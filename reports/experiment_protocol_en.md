# Experiment Protocol: Hyperbolic Field Saccharomyces cerevisiae Study

## Setup

- Model organism: *Saccharomyces cerevisiae* (Dr. Oetker dry yeast, 7g, batch L329 M68)
- Two media types prepared per condition:
  - **N** — neutral solution (growth medium baseline)
  - **P** — nutrient solution (enriched growth medium)
- Samples distributed into 4 channel conditions:
  - **CH0** — control, no field exposure
  - **CH17** — hyperbolic field, channel 17
  - **CH19** — hyperbolic field, channel 19 (time acceleration)
  - **CH21** — hyperbolic field, channel 21 (time deceleration)
- Irradiation duration: 80 minutes (1h 20m) per session
- Container type: Petri dishes
- Environment: basement (−1 floor), complete darkness during irradiation
- Temperature: 10°C (basement irradiation area); 18°C (3rd floor lab)
- Environmental sensors: DHT11 digital (temperature + humidity) placed next to each sample; photoresistors for light monitoring

## Channel Mapping

| Channel | Semantic | Plasma Study Precedent |
|---------|----------|------------------------|
| **CH0 / control** | No field, baseline | Baseline (blood plasma study) |
| **CH17** | Unknown effect (H7) | Not tested in plasma study |
| **CH19** | Time acceleration | Fast clot formation + lysis in plasma |
| **CH21** | Time deceleration | Dense, slow clot in plasma |

## Experiment Cycles (Biological Replicates)

Three independent experiment cycles were conducted:

| Cycle | Label | Description |
|-------|-------|-------------|
| 1 | set 001 | First irradiation batch across all channels |
| 2 | set 002 | Second irradiation batch (biological replicate) |
| 3 | set 003 | Third irradiation batch (biological replicate) |

Sets 001/002/003 are the primary replicate unit for statistical analysis. Each cycle is a separate irradiation event with freshly prepared samples.

## Observation Schedule

| Timepoint | Action |
|-----------|--------|
| Before irradiation (t=0) | Photograph + microscopy |
| Immediately after (~80 min) | Photograph + microscopy |
| 3h post-exposure | Photograph |
| 6h post-exposure | Photograph |
| 12h post-exposure | Photograph + microscopy |
| 24h post-exposure | Photograph + microscopy + staining |
| 48h post-exposure | Photograph + microscopy + staining |

## Microscopy

- Instrument: light microscope with strong LED illumination
- Image capture: smartphone camera through eyepiece, **HEIC format**
- Imaging mode: endpoint photography (not time-lapse)

| Objective | Ring color | Magnification | Use |
|-----------|------------|---------------|-----|
| White ring | белый | 100× | Cell-level morphology and counting |
| Yellow ring | жёлтый | 10× | Field-level overview (occupancy/texture; cell counting not valid at this magnification) |

Note: comparisons must be made within the same magnification level only (100× vs 100×, 10× vs 10×).

## Viability Assay (Registered Protocol)

**Methylene blue staining:**

1. Prepare staining solution: 0.1 mg/mL methylene blue in 2% sodium citrate dihydrate.
2. Mix 100 µL cell suspension + 100 µL staining solution.
3. Incubate 5 minutes at room temperature.
4. Mount on glass slide and image under microscope.
5. Score cells:
   - Dead cells: stain blue (cannot reduce dye)
   - Live cells: remain unstained (enzymatically reduce dye)
   - Budding cells with slight blue tinge: count as live

> **Important caveat:** This is the *registered* viability protocol. The **first analysed microscopy batch (2026-06-09, 990 fields, cycles 001–003) used NO viability stain**. The blue cast observed in those images is from the medium and LED illumination, not from methylene blue. That batch reports **cell density only**, not live/dead viability. Staining, OD600 measurements, and fermentation outcome data remain pending.

## Equipment

| Item | Specification |
|------|---------------|
| Emitter system | 6 nodes, 60W avg / 144W peak, clean sine wave |
| Temperature/humidity sensors | DHT11 digital, one per sample position |
| Light sensors | Photoresistors + ADC |
| Microscope | Light microscope with strong LED illumination |
| Data logging | Linux-based microprocessor, 1 TB storage, auto-logging at 1 measurement/minute (~80 per session) |
| Containers | Petri dishes |
| Staining supplies | Methylene blue 0.1 mg/mL, sodium citrate dihydrate 2%, glass slides |

## Data

- 3 experiment cycles (biological replicates): 001, 002, 003
- 990 microscopy fields analysed in first imaging batch (2026-06-09)
- 4 channel conditions: CH0 (control), CH17, CH19, CH21
- 2 media co-factors: N (neutral), P (nutrient)
- 2 magnifications: 100× (white objective), 10× (yellow objective)
- Image format: HEIC (original), PNG/JPG (processed)

## Failed / Excluded Samples

- Sample **2-0-P1**: failed group — sample spilled / absent (journal dashes confirmed correct). Excluded from analysis.

## Provenance

Protocol parameters extracted from the lab journal and researcher-confirmed semantics.

OSF preregistration: [osf.io/vxkum](https://osf.io/vxkum) (registered Apr 4, 2026; accepted Apr 7, 2026).
Semantics confirmed: 2026-06-09 (cross-checked against microscope-objectives photograph).
