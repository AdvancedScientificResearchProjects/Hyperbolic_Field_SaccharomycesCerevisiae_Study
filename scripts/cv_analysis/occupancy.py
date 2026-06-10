#!/usr/bin/env python3
"""
Segmentation-FREE density metrics for yeast microscopy fields.

Robust to the dataset's huge cell-size / density heterogeneity (sparse large-cell
fields AND confluent lawns of tiny cells) where object counting (cyto2/blob) breaks.
Cells create local texture/edges; empty medium is smooth -> measure that directly:

  texture_energy   = mean local std-dev inside FOV (continuous density proxy)
  texture_occupancy= fraction of FOV with local std above an Otsu threshold
  edge_density     = fraction of FOV that is Canny edge
  bg_contrast      = std of FOV intensity (whole-field heterogeneity)

No threshold-on-cell-size, no segmentation -> comparable across lawns and sparse fields.

Usage:
  python occupancy.py --jpg-dir D --out results/cv_analysis/occupancy.csv
     [--downscale 1600] [--win 11] [--only IMG_x.jpg ...] [--vis-dir D]
"""
import argparse, csv, json, math, time
from pathlib import Path
import numpy as np
import cv2


def load(path, max_side):
    bgr = cv2.imread(str(path))
    if bgr is None:
        return None, None
    h, w = bgr.shape[:2]
    sc = max_side / max(h, w) if max(h, w) > max_side else 1.0
    if sc < 1.0:
        bgr = cv2.resize(bgr, (int(w * sc), int(h * sc)), interpolation=cv2.INTER_AREA)
    return bgr, cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)


def fov_mask(gray):
    h, w = gray.shape
    _, th = cv2.threshold(cv2.GaussianBlur(gray, (0, 0), 2), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return np.ones_like(gray, bool), (w / 2, h / 2, min(w, h) / 2)
    c = max(cnts, key=cv2.contourArea)
    (cx, cy), r = cv2.minEnclosingCircle(c)
    m = np.zeros_like(gray, np.uint8)
    cv2.circle(m, (int(cx), int(cy)), int(r * 0.93), 255, -1)   # tighter to drop bright rim
    return m.astype(bool), (cx, cy, r)


def local_std(gray, k):
    g = gray.astype(np.float32)
    mean = cv2.boxFilter(g, -1, (k, k))
    sq = cv2.boxFilter(g * g, -1, (k, k))
    var = np.clip(sq - mean * mean, 0, None)
    return np.sqrt(var)


def analyze(path, max_side, win, vis_dir=None):
    bgr, gray = load(path, max_side)
    if bgr is None:
        return {"file": Path(path).name, "error": "unreadable"}
    fov, (cx, cy, r) = fov_mask(gray)
    n_fov = int(fov.sum())
    focus = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    lstd = local_std(gray, win)
    inside = lstd[fov]
    # Otsu threshold on the in-FOV local-std distribution -> "textured" (cell) pixels
    vals = inside.astype(np.uint8) if inside.max() <= 255 else (inside / inside.max() * 255).astype(np.uint8)
    thr, _ = cv2.threshold(vals, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    occ = float((vals > thr).mean())
    edges = cv2.Canny(gray, 50, 150)
    edge_density = float((edges[fov] > 0).mean())
    res = {
        "file": Path(path).name, "fov_area_px": n_fov, "focus_var": round(focus, 1),
        "texture_energy": round(float(inside.mean()), 3),
        "texture_occupancy": round(occ, 4),
        "edge_density": round(edge_density, 4),
        "bg_contrast": round(float(gray[fov].std()), 2),
        "mean_intensity": round(float(gray[fov].mean()), 1),
    }
    if vis_dir:
        Path(vis_dir).mkdir(parents=True, exist_ok=True)
        heat = np.zeros_like(gray); heat[fov] = (vals > thr)[:] * 255 if False else 0
        mask = np.zeros_like(gray); mask[fov] = (lstd[fov] > thr).astype(np.uint8) * 255
        ov = bgr.copy(); ov[mask > 0] = (0, 0, 255)
        ov = cv2.addWeighted(bgr, 0.6, ov, 0.4, 0)
        cv2.putText(ov, f"occ={occ:.2f} tex={inside.mean():.1f}", (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imwrite(str(Path(vis_dir) / (Path(path).stem + "_occ.jpg")), ov)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jpg-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--downscale", type=int, default=1600)
    ap.add_argument("--win", type=int, default=11)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--vis-dir")
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
            rows.append(analyze(f, args.downscale, args.win, args.vis_dir))
        except Exception as e:
            rows.append({"file": f.name, "error": str(e)[:200]})
        if k % 100 == 0 or k == len(files):
            print(f"  {k}/{len(files)} ({time.time()-t0:.0f}s)", flush=True)
    keys = sorted({k for r in rows for k in r})
    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); w.writerows(rows)
    json.dump(rows, open(str(args.out).replace(".csv", ".json"), "w"), indent=1)
    print(f"DONE {len([r for r in rows if not r.get('error')])}/{len(rows)} ({time.time()-t0:.0f}s) -> {args.out}")


if __name__ == "__main__":
    main()
