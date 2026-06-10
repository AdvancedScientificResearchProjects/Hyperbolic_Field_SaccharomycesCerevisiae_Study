#!/usr/bin/env python3
"""
Charts for the 2026-06-09 yeast density analysis report.
Reads results/ (white_counts, occupancy_full, llm_full) + the verified journal
mapping, outputs PNGs to charts/. DPI 150. ASRP palette (control green, field red/orange/blue).

Run: python generate_charts.py   (from this report dir)
"""
import csv, json, re, statistics as st, collections, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RES = os.path.join(REPO, "results")
OUT = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(OUT, exist_ok=True)

# ---- channel palette (control = green, fields = warm/cool) ----
COL = {"0": "#2ECC71", "17": "#E74C3C", "19": "#E67E22", "21": "#3498DB"}
LBL = {"0": "CH0\n(control)", "17": "CH17", "19": "CH19", "21": "CH21"}
ORDER = ["0", "17", "19", "21"]


def mapping():
    m = {}
    with open(os.path.join(REPO, "data/photos/journal-mapping.csv")) as f:
        for r in csv.DictReader(f):
            try:
                a, b = int(r["img_start"]), int(r["img_end"])
            except Exception:
                continue
            if a == 0:
                continue
            for n in range(a, b + 1):
                m[n] = (r["channel"], r["set"], r.get("zone", "—"))
    return m


def num(fn):
    return int(re.search(r"IMG_(\d+)", fn).group(1))


M = mapping()


def load_rows(path, key):
    out = {}
    with open(path) as f:
        for r in csv.DictReader(f):
            if r.get("error"):
                continue
            try:
                out[r["file"]] = float(r[key])
            except Exception:
                pass
    return out


# ============================================================ chart 1: counts 100x by channel
def chart_counts_100x():
    wc = load_rows(os.path.join(RES, "cv_analysis/white_counts.csv"), "cell_count")
    g = collections.defaultdict(list)
    for fn, v in wc.items():
        mm = M.get(num(fn))  # defensive: only 100× (белый), cycles 2&3
        if mm and mm[2] == "белый" and mm[1] in ("2", "3") and mm[0] in COL:
            g[mm[0]].append(v)
    means = [st.mean(g[c]) for c in ORDER]
    sems = [st.pstdev(g[c]) / np.sqrt(len(g[c])) for c in ORDER]
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar([LBL[c] for c in ORDER], means, yerr=sems, capsize=5,
                  color=[COL[c] for c in ORDER], edgecolor="black", linewidth=0.7)
    for c, b, v in zip(ORDER, bars, means):
        ax.text(b.get_x() + b.get_width() / 2, v + max(means) * 0.02, f"{v:.0f}\n(n={len(g[c])})",
                ha="center", va="bottom", fontsize=9)
    ax.axhline(means[0], ls="--", color="gray", lw=1, alpha=0.7)
    ax.set_ylabel("Mean cells per field (cyto2, 100×)\nerror = per-field SEM (descriptive; replicate n=2 cycles)")
    ax.set_title("Cell count by channel — 100× (cyto2 segmentation)\nСчёт клеток по каналам — 100×")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "chart_counts_100x.png"), dpi=150); plt.close(fig)


# ============================================================ chart 2: occupancy by magnification
def chart_occupancy_by_mag():
    occ = load_rows(os.path.join(RES, "cv_analysis/occupancy_full.csv"), "texture_occupancy")
    data = {}  # zone -> ch -> mean
    for zn, nm in [("белый", "100×"), ("жёлтый", "10×")]:
        g = collections.defaultdict(list)
        for fn, v in occ.items():
            mm = M.get(num(fn))
            if mm and mm[2] == zn and mm[0] in COL:
                g[mm[0]].append(v)
        data[nm] = {c: st.mean(g[c]) for c in ORDER if g.get(c)}
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(ORDER)); w = 0.38
    import matplotlib.patches as mpatches
    for i, nm in enumerate(["10×", "100×"]):
        vals = [data[nm].get(c, np.nan) for c in ORDER]
        ax.bar(x + (i - 0.5) * w, vals, w,
               color=[COL[c] for c in ORDER], edgecolor="black", alpha=0.65 + 0.35 * i, linewidth=0.7)
    ax.set_xticks(x); ax.set_xticklabels([LBL[c] for c in ORDER])
    ax.set_ylabel("Texture occupancy (density proxy)")
    ax.set_title("Occupancy density by channel & magnification (787 mag-labelled fields)\nПлотность по каналам и увеличению")
    h10 = mpatches.Patch(facecolor="gray", alpha=0.65, edgecolor="black", label="10×")
    h100 = mpatches.Patch(facecolor="gray", alpha=1.0, edgecolor="black", label="100×")
    ax.legend(handles=[h10, h100], title="Magnification")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "chart_occupancy_by_magnification.png"), dpi=150); plt.close(fig)


# ============================================================ chart 3: per-cycle counts 100x
def chart_by_cycle():
    wc = load_rows(os.path.join(RES, "cv_analysis/white_counts.csv"), "cell_count")
    g = collections.defaultdict(list)  # (cycle,ch)->[]
    for fn, v in wc.items():
        mm = M.get(num(fn))
        if mm and mm[0] in COL:
            g[(mm[1], mm[0])].append(v)
    cycles = sorted({c for (c, _) in g})
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(cycles)); w = 0.2
    for i, ch in enumerate(ORDER):
        vals = [st.mean(g[(cy, ch)]) if g.get((cy, ch)) else float("nan") for cy in cycles]
        ax.bar(x + (i - 1.5) * w, vals, w, label=LBL[ch].replace("\n", " "),
               color=COL[ch], edgecolor="black", linewidth=0.6)
    ax.set_xticks(x); ax.set_xticklabels([f"Cycle {c}" for c in cycles])
    ax.set_ylabel("Mean cells per field (100×)")
    ax.set_title("Cell count by channel, per experiment cycle (100×)\nСчёт по каналам в каждом цикле")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "chart_counts_by_cycle.png"), dpi=150); plt.close(fig)


# ============================================================ chart 4: method correlation (CV vs LLM, 100x)
def chart_method_corr():
    wc = load_rows(os.path.join(RES, "cv_analysis/white_counts.csv"), "cell_count")
    llm = {r["file"]: r for r in json.load(open(os.path.join(RES, "llm_full/llm_full.json")))["records"]}
    xs, ys, cs = [], [], []
    for fn, cv in wc.items():
        if fn in llm and isinstance(llm[fn].get("cell_estimate"), (int, float)):
            ch = M.get(num(fn), (None,))[0]
            if ch in COL:
                xs.append(cv); ys.append(llm[fn]["cell_estimate"]); cs.append(COL[ch])
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.scatter(xs, ys, c=cs, s=22, alpha=0.7, edgecolor="black", linewidth=0.3)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("CV cell count (cyto2)"); ax.set_ylabel("LLM cell estimate")
    from scipy.stats import spearmanr
    rho, _ = spearmanr(xs, ys)
    ax.set_title(f"CV vs LLM agreement, 100× (Spearman ρ={rho:.2f}, n={len(xs)})\nСогласие CV и LLM")
    handles = [plt.Line2D([], [], marker="o", ls="", color=COL[c], label=LBL[c].replace("\n", " ")) for c in ORDER]
    ax.legend(handles=handles, fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "chart_cv_vs_llm.png"), dpi=150); plt.close(fig)


# ============================================================ chart 5: relative effect vs control
def chart_relative_effect():
    wc = load_rows(os.path.join(RES, "cv_analysis/white_counts.csv"), "cell_count")
    g = collections.defaultdict(list)
    for fn, v in wc.items():
        mm = M.get(num(fn))  # defensive: only 100× (белый), cycles 2&3
        if mm and mm[2] == "белый" and mm[1] in ("2", "3") and mm[0] in COL:
            g[mm[0]].append(v)
    base = st.mean(g["0"])
    fields = ["17", "19", "21"]
    delta = [(st.mean(g[c]) / base - 1) * 100 for c in fields]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.barh([LBL[c].replace("\n", " ") for c in fields], delta,
                   color=[COL[c] for c in fields], edgecolor="black", linewidth=0.7)
    for b, d in zip(bars, delta):
        # label always on the positive side of the bar tip, reading away from 0
        x = d + 1.5 if d >= 0 else d + 1.5
        ax.text(x, b.get_y() + b.get_height() / 2, f"{d:+.0f}%",
                va="center", ha="left", fontsize=10, fontweight="bold")
    ax.set_xlim(min(delta) - 12, max(delta) + 18)
    ax.axvline(0, color="gray", lw=1)
    ax.set_xlabel("% cell count vs control (100×)")
    ax.set_title("Field effect on cell density vs control\nЭффект поля относительно контроля")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "chart_relative_effect.png"), dpi=150); plt.close(fig)


if __name__ == "__main__":
    chart_counts_100x()
    chart_occupancy_by_mag()
    chart_by_cycle()
    chart_method_corr()
    chart_relative_effect()
    print("charts ->", OUT)
    for f in sorted(os.listdir(OUT)):
        print("  ", f)
