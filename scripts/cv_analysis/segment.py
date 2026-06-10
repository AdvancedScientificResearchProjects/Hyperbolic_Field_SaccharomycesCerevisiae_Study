#!/usr/bin/env python3
"""
Yeast microscopy CV segmentation + per-image metrics. Group-AGNOSTIC.

Backends:
  --method blob (DEFAULT): downscale -> FOV mask -> CLAHE -> Laplacian-of-Gaussian
      blob detection (skimage blob_log) with sigma matched to cell radius. Ignores
      sub-cell texture noise (below min_sigma). Fast (~1 s/image at 1024 px), no GPU.
  --method cellpose: Cellpose CNN (cyto2/cyto3 if cellpose<4; CPSAM if 4.x). Accurate
      but heavier; use for a validation subset.

Per image: cell count, density (cells per FOV megapixel + fractional coverage),
area stats, spatial clustering (Clark-Evans), focus quality, per-cell brightness/
saturation (raw; live/dead deferred until stain protocol confirmed).

Usage:
  python segment.py --jpg-dir D --out results/cv.csv [--method blob|cellpose]
     [--downscale 1100] [--blob-min 2.5 --blob-max 12 --blob-thresh 0.08]
     [--only IMG_x.jpg ...] [--limit N] [--vis-dir D] [--cpu]
"""
import argparse, csv, json, math, time
from pathlib import Path
import numpy as np
import cv2


def load_downscaled(path, max_side):
    bgr = cv2.imread(str(path))
    if bgr is None:
        return None, None, 1.0
    h, w = bgr.shape[:2]
    sc = max_side / max(h, w) if max(h, w) > max_side else 1.0
    if sc < 1.0:
        bgr = cv2.resize(bgr, (int(w * sc), int(h * sc)), interpolation=cv2.INTER_AREA)
    return bgr, cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY), sc


def fov_mask(gray):
    h, w = gray.shape
    _, th = cv2.threshold(cv2.GaussianBlur(gray, (0, 0), 2), 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return np.ones_like(gray, bool), (w / 2, h / 2, min(w, h) / 2), 0.0
    c = max(cnts, key=cv2.contourArea)
    (cx, cy), r = cv2.minEnclosingCircle(c)
    m = np.zeros_like(gray, np.uint8)
    cv2.circle(m, (int(cx), int(cy)), int(r * 0.95), 255, -1)
    circ = cv2.contourArea(c) / (math.pi * r * r + 1e-9)
    return m.astype(bool), (cx, cy, r), float(circ)


# ----------------------------------------------------------- blob backend
def cells_blob(gray, fov, min_sigma, max_sigma, thresh):
    from skimage.feature import blob_log
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8)).apply(gray)
    g = (clahe.astype(np.float32) / 255.0)
    blobs = blob_log(g, min_sigma=min_sigma, max_sigma=max_sigma, num_sigma=8, threshold=thresh)
    out = []
    for y, x, s in blobs:
        if not fov[int(y), int(x)]:
            continue
        r = s * math.sqrt(2)
        out.append({"cx": float(x), "cy": float(y), "r": float(r),
                    "area": float(math.pi * r * r), "solidity": 1.0})
    return out


# ----------------------------------------------------------- cellpose backend
_MODEL = None
def cells_cellpose(rgb, gray, fov, gpu, diameter=0):
    global _MODEL
    if _MODEL is None:
        from cellpose import models
        try:  # cellpose 3.x CNN
            _MODEL = models.Cellpose(gpu=gpu, model_type="cyto2")
            _MODEL = ("v3", _MODEL)
        except Exception:
            _MODEL = ("v4", models.CellposeModel(gpu=gpu))
    ver, model = _MODEL
    diam = diameter if diameter and diameter > 0 else None
    if ver == "v3":
        masks, _, _, _ = model.eval(gray, diameter=diam, channels=[0, 0])
    else:
        masks = model.eval(gray, diameter=diam)[0]
    from skimage.measure import regionprops
    out = []
    for i in np.unique(masks):
        if i == 0:
            continue
        ys, xs = np.where(masks == i)
        if len(xs) < 8:
            continue
        ccx, ccy = float(xs.mean()), float(ys.mean())
        if not fov[int(ccy), int(ccx)]:
            continue
        m = (masks == i).astype(np.uint8)
        cnt, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sol = None
        if cnt:
            c = max(cnt, key=cv2.contourArea)
            hull = cv2.contourArea(cv2.convexHull(c))
            sol = float(cv2.contourArea(c) / (hull + 1e-9)) if hull else None
        # morphometrics via regionprops
        props = regionprops(m)
        ecc = float(props[0].eccentricity) if props else None
        maj = float(props[0].axis_major_length) if props else None
        minn = float(props[0].axis_minor_length) if props else None
        ar = float(maj / minn) if (maj is not None and minn and minn > 0) else None
        out.append({"cx": ccx, "cy": ccy, "area": float(len(xs)), "solidity": sol,
                    "r": math.sqrt(len(xs) / math.pi),
                    "eccentricity": ecc, "aspect_ratio": ar})
    return out


def clark_evans(cells, area_px):
    if len(cells) < 3:
        return None
    from scipy.spatial import cKDTree
    pts = np.array([(c["cx"], c["cy"]) for c in cells], float)
    d, _ = cKDTree(pts).query(pts, k=2)
    rho = len(cells) / area_px
    r_exp = 1.0 / (2.0 * math.sqrt(rho)) if rho > 0 else None
    return round(float(d[:, 1].mean() / r_exp), 4) if r_exp else None


def analyze(path, args):
    bgr, gray, sc = load_downscaled(path, args.downscale)
    if bgr is None:
        return {"file": Path(path).name, "error": "unreadable"}
    H, W = gray.shape
    fov, (cx, cy, r), fov_circ = fov_mask(gray)
    fov_area = int(fov.sum())
    focus = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    if args.method == "cellpose":
        cells = cells_cellpose(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB), gray, fov, not args.cpu, getattr(args,"cp_diameter",0))
    else:
        cells = cells_blob(gray, fov, args.blob_min, args.blob_max, args.blob_thresh)
    # per-cell color
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    for c in cells:
        rr = max(2, int(c["r"]))
        y0, y1 = max(0, int(c["cy"]) - rr), min(H, int(c["cy"]) + rr)
        x0, x1 = max(0, int(c["cx"]) - rr), min(W, int(c["cx"]) + rr)
        patch = hsv[y0:y1, x0:x1]
        c["gray"] = float(gray[y0:y1, x0:x1].mean()) if patch.size else 0.0
        c["sat"] = float(patch[:, :, 1].mean()) if patch.size else 0.0
    n = len(cells)
    cell_px = sum(c["area"] for c in cells)
    res = {"file": Path(path).name, "method": args.method, "scale": round(sc, 3),
           "width": W, "height": H, "fov_r": round(r, 1), "fov_area_px": fov_area,
           "fov_circularity": round(fov_circ, 3), "focus_var": round(focus, 1),
           "cell_count": n,
           "cell_density_per_Mpx": round(n / (fov_area / 1e6), 1) if fov_area else None,
           "coverage_frac": round(cell_px / fov_area, 4) if fov_area else None}
    if n:
        a = np.array([c["area"] for c in cells], float)
        g = np.array([c["gray"] for c in cells], float)
        s = np.array([c["sat"] for c in cells], float)
        sols = np.array([c["solidity"] for c in cells if c["solidity"] is not None], float)
        eccs = np.array([c["eccentricity"] for c in cells
                         if c.get("eccentricity") is not None], float)
        ars = np.array([c["aspect_ratio"] for c in cells
                        if c.get("aspect_ratio") is not None], float)
        res.update({"area_mean_px": round(a.mean(), 1), "area_median_px": round(float(np.median(a)), 1),
                    "cell_gray_mean": round(g.mean(), 1), "cell_sat_mean": round(s.mean(), 1),
                    "budding_proxy_frac": round(float((sols < 0.90).mean()), 3) if len(sols) and sols.min() < 1 else None,
                    "clustering_R": clark_evans(cells, fov_area),
                    "ecc_mean": round(float(eccs.mean()), 4) if len(eccs) else None,
                    "ecc_median": round(float(np.median(eccs)), 4) if len(eccs) else None,
                    "aspect_ratio_mean": round(float(ars.mean()), 4) if len(ars) else None})
    if args.vis_dir:
        Path(args.vis_dir).mkdir(parents=True, exist_ok=True)
        ov = bgr.copy()
        for c in cells:
            cv2.circle(ov, (int(c["cx"]), int(c["cy"])), max(2, int(c["r"])), (0, 0, 255), 1)
        cv2.circle(ov, (int(cx), int(cy)), int(r), (0, 255, 0), 1)
        cv2.putText(ov, f"n={n}", (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imwrite(str(Path(args.vis_dir) / (Path(path).stem + "_seg.jpg")), ov)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jpg-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--method", choices=["blob", "cellpose"], default="blob")
    ap.add_argument("--downscale", type=int, default=1100)
    ap.add_argument("--blob-min", type=float, default=2.5)
    ap.add_argument("--blob-max", type=float, default=12.0)
    ap.add_argument("--blob-thresh", type=float, default=0.08)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--vis-dir")
    ap.add_argument("--cpu", action="store_true")
    ap.add_argument("--cp-diameter", type=float, default=0)
    args = ap.parse_args()
    files = sorted(Path(args.jpg_dir).glob("*.jpg"))
    if args.only:
        files = [f for f in files if f.name in set(args.only)]
    if args.limit:
        files = files[: args.limit]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    rows, t0 = [], time.time()
    for k, f in enumerate(files, 1):
        try:
            rows.append(analyze(f, args))
        except Exception as e:
            rows.append({"file": f.name, "error": str(e)[:200]})
        if k % 50 == 0 or k == len(files):
            print(f"  {k}/{len(files)} ({time.time()-t0:.0f}s)", flush=True)
    keys = sorted({k for r in rows for k in r})
    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); w.writerows(rows)
    json.dump(rows, open(str(args.out).replace(".csv", ".json"), "w"), indent=1)
    ok = [r for r in rows if "error" not in r]
    print(f"DONE {len(ok)}/{len(rows)} ok ({time.time()-t0:.0f}s) -> {args.out}")
    if ok:
        cc = sorted(r["cell_count"] for r in ok if r.get("cell_count") is not None)
        print(f"  cell_count: min={cc[0]} med={cc[len(cc)//2]} max={cc[-1]}")


if __name__ == "__main__":
    main()
