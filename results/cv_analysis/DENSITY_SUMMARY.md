# Yeast density analysis — preliminary signal (2026-06-09)

## Methods (triangulation, all group-AGNOSTIC measurement, channel revealed only at aggregation)
1. Blind LLM single-image scoring (3 analysts/image), 2 independent samples (n=24 each, 0 overlap).
2. Occupancy density (segmentation-free: local texture energy + Otsu occupancy + edge density) on ALL 972 fields. Robust to the dataset's huge cell-size heterogeneity (sparse fields AND confluent lawns), where cyto2/blob counting fails (e.g. IMG_5170 = packed lawn, cyto2 counted 3).

## Result — reproducible directional ordering (sets 2 & 3)
Occupancy mean, ch17 top / ch21 bottom in EVERY slice:
- set2:        ch17 0.546 > ch0 0.452 > ch19 0.439 > ch21 0.286
- set3:        ch17 0.502 > ch19 0.468 > ch0 0.451 > ch21 0.414
- exposure N:  ch17 0.554 > ch19 0.497 > ch0 0.485 > ch21 0.427
- exposure P:  ch17 0.480 > ch19 0.421 > ch0 0.393 > ch21 0.282
- zone белый:  ch17 0.433 > ch19 0.342 > ch0 0.321 > ch21 0.259
- zone жёлтый: ch17 0.608 > ch0 0.580 > ch19 0.572 > ch21 0.460
Blind LLM (2 runs): ch17 highest, ch21 lowest both times.

=> ch17 densest, ch21 sparsest (consistently BELOW control ch0), ch19 ~ control.
Consistency: ch17 top / ch21 bottom in cycles 2 AND 3 (the only independent replicates). NOTE: the "6 slices" (set2/set3/exp-N/exp-P/белый/жёлтый) are 3 re-partitions of the SAME cyc2+cyc3 pool = 2 biological replicates, not 6 independent confirmations. Cycle 1 reverses the ordering (see UPDATE 2). Formal claim: agrees in 2 of 3 cycles.

## Directional match to protocol hypothesis
CH21 = "deceleration" -> lowest density (below control) ✓ consistent.
CH17 = "unknown" -> turns out highest. CH19 = "acceleration" -> ~control (flat here).
NOTE: "flat" count is the EXPECTED outcome for CH19 — its pre-registered role is division rate/dynamics, not count/biomass increase (that is CH17). See report_en.md §9.

## CAVEATS (this is PRELIMINARY, not proof)
- Pseudoreplication: many fields, only ~2 biological replicates (N/P? replicate 1/2?) -> p-values (Kruskal p<1e-4) are inflated, NOT valid significance.
- Semantics pending researcher confirmation: meaning of N/P, sets 001/002/003, zones белый/жёлтый; stain identity (images look methylene-blue, journal says white/yellow).
- Possible imaging/prep confounds per channel not excluded.
- set1 (page A/B, separate session) does NOT follow the ordering (ch21 highest there).
- Density only; viability deferred (stain unconfirmed).

## UPDATE 2026-06-09 — semantics confirmed + cycle-level (replicate) analysis
Researcher-confirmed: N=neutral medium, P=nutrient medium; sets 001/002/003 = experiment CYCLES (replicates); zones белый=100× / жёлтый=10× magnification; 2-0-P1 failed (spilled); no viability stain (blue = medium, not dye).

Replicate-level density ranking (occupancy), cycles 2 & 3 × both magnifications (4 blocks):
- ch17 rank 1 in 4/4 blocks (mean rank 1.00) — densest every time
- ch21 rank 4 in 4/4 blocks (mean rank 4.00) — sparsest every time, below control
- ch19 mean rank 2.25 ; control(ch0) mean rank 2.75
Per-block ordering:
- cyc2 100×: ch17>ch19>ch0>ch21 ; cyc3 100×: ch17>ch19>ch0>ch21
- cyc2 10× : ch17>ch0>ch19>ch21 ; cyc3 10× : ch17>ch19>ch0>ch21
- cyc1 (no-mag, page A/B, different protocol) DISAGREES: ch21>ch17>ch0>ch19

VERDICT: reproducible directional signal CH17↑ (densest) / CH21↓ (below control) across 2 of 3 cycles, both media, both magnifications, + 2 blind-LLM runs. Directionally matches protocol (CH21 deceleration). NOT confirmatory: only 3 cycles, cycle 1 contradicts (needs explanation), no hard significance claim.

## UPDATE 2 (2026-06-09) — magnification-aware CV (proper counting)
Fixed cyto2 by splitting magnification + calibrating diameter (cells uncountable at 10× lawns; countable at 100×).

### 100× (белый) — cyto2 CELL COUNT (diam=18), n=82–112/channel
- ch0 (control): mean 112 (median 107)
- ch17: mean 205 (median 196)  -> +83% vs control
- ch19: mean 118 (median 116)  -> ≈ control
- ch21: mean 88  (median 78)   -> -21% vs control
Per cycle: cyc2 ch17=226/ch21=64 ; cyc3 ch17=191/ch21=109 (ch17 top & ch21 bottom in BOTH).
Descriptive stats (pseudoreplication!): control vs ch17 p<1e-4 ; vs ch21 p=0.0017 ; vs ch19 p=0.39.

### 10× (жёлтый) — occupancy, n=83–109/channel
ch17 0.608 > ch0 0.580 ≈ ch19 0.572 > ch21 0.460. Same ordering, both cycles.

### CONVERGENT VERDICT
Across BOTH magnifications × BOTH cycles × BOTH CV methods (count + occupancy) and 2 blind-LLM runs:
  CH17 = strongest (≈1.8× control by count) ; CH21 = below control ; CH19 ≈ control.
Directional match to protocol: CH21 "deceleration" -> fewer cells (clean); CH17 (was "unknown") -> strongest enhancer; CH19 "acceleration" -> flat here.
NOTE: "flat" count is the EXPECTED outcome for CH19 — its pre-registered role is division rate/dynamics, not count/biomass increase (that is CH17). See report_en.md §9.
CV cell-count is far more discriminating than the LLM (which saturated at "high").

### Still preliminary
N=2 cycles (sets 2,3); p-values descriptive only (pseudoreplication); evidence = cross-cycle/-magnification CONSISTENCY, not significance. cyto2 ~40% systematic undercount (relative comparison valid). Need ≥5 cycles for confirmatory claim.
