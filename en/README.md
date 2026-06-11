# Hyperbolic Field Saccharomyces cerevisiae Study — Data Browse Hub

**🌐 Language / Язык:** **English** · [Русский](../ru/README.md)

Experimental datasets, microscopy images, and analytical materials from *Saccharomyces cerevisiae*
exposure to hyperbolic field emitters. Includes raw microscopy fields, journal-mapped sample
identification, CV and LLM density analysis, and protocol references.

---

## How to Browse Data

1. **Select a condition group** → table below; each row identifies channel, medium, cycle, and magnification
2. **Look up image numbers** → use the [IMG Numbering / Sample-ID Spec](#img-numbering--sample-id-spec) below to map `IMG_XXXX` to channel / medium / cycle / zone via `journal-mapping.csv`
3. **Browse JPEG previews** → `data/photos/jpg/` — 972 JPEG files for browser viewing; originals (HEIC/PNG) in `data/photos/original/`
4. **Read the density report** → `reports/2026-06-09_density-analysis/report_en.md` — triangulated CV + LLM analysis across all 972 fields
5. **Machine-readable metadata** → `data/photos/manifest.json`; journal mapping → `data/photos/journal-mapping.csv`

---

## Condition Groups

The microscopy set spans **3 experiment cycles** (sets 001–003), **4 channels** (CH0 control / CH17 / CH19 / CH21),
**2 media** (N = neutral, P = nutrient), and **2 magnifications** (100× white-ring objective / 10× yellow-ring objective).
Set 002 and Set 003 have a two-zone layout (zone белый = 100×, zone жёлтый = 10×); Set 001 (page A/B session)
has no magnification split.

| Group ID | Set / Cycle | Channel | Medium | Replicate | Zone (Magnification) | IMG range | Count | Notes |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| S1-ch0-N2 | 001 | CH0 (control) | N | 2 | — | 4801–4806 | 6 | |
| S1-ch0-N1 | 001 | CH0 (control) | N | 1 | — | 4807–4812 | 6 | |
| S1-ch0-P2 | 001 | CH0 (control) | P | 2 | — | 4813–4818 | 6 | |
| S1-ch0-P1 | 001 | CH0 (control) | P | 1 | — | 4820–4825 | 6 | 4819 struck in journal |
| S1-ch17-N1 | 001 | CH17 | N | 1 | — | 4826–4837 | 12 | |
| S1-ch17-P1 | 001 | CH17 | P | 1 | — | 4838–4847 + 4983–4987 | 14 | Non-contiguous; 4847 struck (block divider) |
| S1-ch17-P2 | 001 | CH17 | P | 2 | — | 4848–4869 | 20 | Skips 4857 (absent on disk) and 4868 (present but unlogged) |
| S1-ch17-N2 | 001 | CH17 | N | 2 | — | 4870–4883 | 14 | |
| S1-ch19-P1 | 001 | CH19 | P | 1 | — | 4884–4895 | 12 | |
| S1-ch19-P2 | 001 | CH19 | P | 2 | — | 4896–4907 | 12 | |
| S1-ch19-N1 | 001 | CH19 | N | 1 | — | 4908–4919 | 12 | |
| S1-ch19-N2 | 001 | CH19 | N | 2 | — | 4920–4931 | 12 | |
| S1-ch21-P1 | 001 | CH21 | P | 1 | — | 4932–4944 | 12 | IMG_4941 absent on disk (disk-confirmed skip) |
| S1-ch21-P2 | 001 | CH21 | P | 2 | — | 4945–4956 | 12 | |
| S1-ch21-N1 | 001 | CH21 | N | 1 | — | 4957–4968 | 12 | |
| S1-ch21-N2 | 001 | CH21 | N | 2 | — | 4969–4981 | 11 | Skip 4971 per journal |
| S2-ch17-P1-белый | 002 | CH17 | P | 1 | 100× (белый) | 5070–5079 | 10 | |
| S2-ch17-P1-жёлтый | 002 | CH17 | P | 1 | 10× (жёлтый) | 5080–5089 | 10 | |
| S2-ch17-P2-жёлтый | 002 | CH17 | P | 2 | 10× (жёлтый) | 5091–5099 | 9 | Gap 5090 = unlogged frame |
| S2-ch17-P2-белый | 002 | CH17 | P | 2 | 100× (белый) | 5100–5109 | 10 | End digit slip in journal, image-confirmed |
| S2-ch0-P2-белый | 002 | CH0 (control) | P | 2 | 100× (белый) | 5110–5120 | 11 | |
| S2-ch0-P2-жёлтый | 002 | CH0 (control) | P | 2 | 10× (жёлтый) | 5121–5129 | 9 | |
| S2-ch0-P1-белый | 002 | CH0 (control) | P | 1 | 100× (белый) | — | 0 | BLANK — sample spilled (failed group) |
| S2-ch0-P1-жёлтый | 002 | CH0 (control) | P | 1 | 10× (жёлтый) | — | 0 | BLANK — sample spilled (failed group) |
| S2-ch0-N1-жёлтый | 002 | CH0 (control) | N | 1 | 10× (жёлтый) | 5130–5141 | 12 | 5142 = unlogged frame |
| S2-ch0-N1-белый | 002 | CH0 (control) | N | 1 | 100× (белый) | 5143–5153 | 11 | |
| S2-ch17-N1-белый | 002 | CH17 | N | 1 | 100× (белый) | 5154–5166 | 13 | |
| S2-ch17-N1-жёлтый | 002 | CH17 | N | 1 | 10× (жёлтый) | 5167–5179 | 13 | Overwritten start digit |
| S2-ch17-N2-жёлтый | 002 | CH17 | N | 2 | 10× (жёлтый) | 5180–5189 | 10 | |
| S2-ch17-N2-белый | 002 | CH17 | N | 2 | 100× (белый) | 5190–5201 | 12 | |
| S2-ch0-N2-белый | 002 | CH0 (control) | N | 2 | 100× (белый) | 5202–5218 | 17 | |
| S2-ch0-N2-жёлтый | 002 | CH0 (control) | N | 2 | 10× (жёлтый) | 5219–5232 | 14 | |
| S2-ch19-P1-жёлтый | 002 | CH19 | P | 1 | 10× (жёлтый) | 5235–5251 | 17 | |
| S2-ch19-P1-белый | 002 | CH19 | P | 1 | 100× (белый) | 5252–5265 | 14 | |
| S2-ch21-P1-жёлтый | 002 | CH21 | P | 1 | 10× (жёлтый) | 5266–5273 | 8 | |
| S2-ch21-P1-белый | 002 | CH21 | P | 1 | 100× (белый) | 5274–5283 | 10 | |
| S2-ch19-P2-белый | 002 | CH19 | P | 2 | 100× (белый) | 5284–5295 | 12 | |
| S2-ch19-P2-жёлтый | 002 | CH19 | P | 2 | 10× (жёлтый) | 5296–5307 | 12 | |
| S2-ch21-P2-жёлтый | 002 | CH21 | P | 2 | 10× (жёлтый) | 5308–5318 | 11 | |
| S2-ch21-P2-белый | 002 | CH21 | P | 2 | 100× (белый) | 5319–5327 | 9 | Bold-overwritten; disk-corrected end (5327) |
| S2-ch21-N1-жёлтый | 002 | CH21 | N | 1 | 10× (жёлтый) | 5334–5344 | 11 | |
| S2-ch21-N1-белый | 002 | CH21 | N | 1 | 100× (белый) | 5345–5356 | 12 | Bold-overwritten both ends |
| S2-ch19-N1-жёлтый | 002 | CH19 | N | 1 | 10× (жёлтый) | 5357–5364 | 8 | |
| S2-ch19-N2-жёлтый | 002 | CH19 | N | 2 | 10× (жёлтый) | 5365–5375 | 11 | |
| S2-ch19-N2-белый | 002 | CH19 | N | 2 | 100× (белый) | 5376–5387 | 12 | Researcher-confirmed anchor |
| S2-ch19-N1-белый | 002 | CH19 | N | 1 | 100× (белый) | 5388–5398 | 11 | |
| S2-ch21-N2-белый | 002 | CH21 | N | 2 | 100× (белый) | 5399–5411 | 13 | Thin end digit, contiguity-resolved |
| S2-ch21-N2-жёлтый | 002 | CH21 | N | 2 | 10× (жёлтый) | 5412–5419 | 8 | |
| S3-ch17-P2-жёлтый | 003 | CH17 | P | 2 | 10× (жёлтый) | 5420–5430 | 11 | |
| S3-ch17-P2-белый | 003 | CH17 | P | 2 | 100× (белый) | 5431–5444 | 14 | |
| S3-ch0-P2-белый | 003 | CH0 (control) | P | 2 | 100× (белый) | 5445–5452 | 8 | |
| S3-ch0-P2-жёлтый | 003 | CH0 (control) | P | 2 | 10× (жёлтый) | 5453–5461 | 9 | |
| S3-ch17-P1-жёлтый | 003 | CH17 | P | 1 | 10× (жёлтый) | 5462–5489 | 28 | |
| S3-ch17-P1-белый | 003 | CH17 | P | 1 | 100× (белый) | 5490–5502 | 13 | Researcher-confirmed anchor |
| S3-ch0-P1-белый | 003 | CH0 (control) | P | 1 | 100× (белый) | 5503–5514 | 12 | |
| S3-ch0-P1-жёлтый | 003 | CH0 (control) | P | 1 | 10× (жёлтый) | 5515–5526 | 12 | |
| S3-ch17-N1-жёлтый | 003 | CH17 | N | 1 | 10× (жёлтый) | 5527–5541 | 15 | |
| S3-ch17-N1-белый | 003 | CH17 | N | 1 | 100× (белый) | 5542–5557 | 16 | |
| S3-ch17-N2-белый | 003 | CH17 | N | 2 | 100× (белый) | 5558–5581 | 24 | Disputed end digit; resolved by partition |
| S3-ch17-N2-жёлтый | 003 | CH17 | N | 2 | 10× (жёлтый) | 5582–5594 | 13 | |
| S3-ch0-N1-жёлтый | 003 | CH0 (control) | N | 1 | 10× (жёлтый) | 5595–5608 | 14 | |
| S3-ch0-N1-белый | 003 | CH0 (control) | N | 1 | 100× (белый) | 5609–5620 | 12 | |
| S3-ch0-N2-белый | 003 | CH0 (control) | N | 2 | 100× (белый) | 5621–5631 | 11 | |
| S3-ch0-N2-жёлтый | 003 | CH0 (control) | N | 2 | 10× (жёлтый) | 5632–5644 | 13 | |
| S3-ch19-P1-жёлтый | 003 | CH19 | P | 1 | 10× (жёлтый) | 5645–5655 | 11 | |
| S3-ch19-P1-белый | 003 | CH19 | P | 1 | 100× (белый) | 5658–5680 | 23 | Small gap 5656–5657 before group |
| S3-ch19-P2-белый | 003 | CH19 | P | 2 | 100× (белый) | 5681–5696 | 16 | |
| S3-ch19-P2-жёлтый | 003 | CH19 | P | 2 | 10× (жёлтый) | 5697–5711 | 15 | |
| S3-ch21-P1-жёлтый | 003 | CH21 | P | 1 | 10× (жёлтый) | 5712–5722 | 11 | |
| S3-ch21-P1-белый | 003 | CH21 | P | 1 | 100× (белый) | 5723–5735 | 13 | |
| S3-ch21-P2-белый | 003 | CH21 | P | 2 | 100× (белый) | 5736–5747 | 12 | |
| S3-ch21-P2-жёлтый | 003 | CH21 | P | 2 | 10× (жёлтый) | 5748–5761 | 14 | |
| S3-ch19-N1-жёлтый | 003 | CH19 | N | 1 | 10× (жёлтый) | 5762–5775 | 14 | |
| S3-ch19-N1-белый | 003 | CH19 | N | 1 | 100× (белый) | 5776–5782 | 7 | |
| S3-ch19-N2-белый | 003 | CH19 | N | 2 | 100× (белый) | 5783–5797 | 15 | |
| S3-ch19-N2-жёлтый | 003 | CH19 | N | 2 | 10× (жёлтый) | 5798–5816 | 19 | |
| S3-ch21-N2-жёлтый | 003 | CH21 | N | 2 | 10× (жёлтый) | 5817–5829 | 13 | |
| S3-ch21-N2-белый | 003 | CH21 | N | 2 | 100× (белый) | 5830–5838 | 9 | |
| S3-ch21-N1-белый | 003 | CH21 | N | 1 | 100× (белый) | 5839–5854 | 16 | |
| S3-ch21-N1-жёлтый | 003 | CH21 | N | 1 | 10× (жёлтый) | 5855–5868 | 14 | Max IMG on disk |

**Total microscopy fields (journal-mapped): ~990**  
(972 HEIC + 18 PNG equipment/staining/microscopy; a small number of present-but-unlogged frames exist on disk
at 4847, 4868, 5090, 5142, 5657 and are not part of any group mapping.)

---

## IMG Numbering / Sample-ID Spec

**Format:** `IMG_XXXX` where XXXX is a 4-digit sequential iPhone camera roll number.

**Mapping source:** `../data/photos/journal-mapping.csv`
(use `.verified.csv` — not the unverified draft; the verified file is the authoritative mapping.)

**Decoding an image number:**

1. Open `journal-mapping.csv`.
2. Find the row where `img_start <= XXXX <= img_end` (accounting for known skips listed in the `notes` column).
3. Read `channel`, `exposure` (medium: N or P), `set` (cycle: 1/2/3), `zone` (белый = 100×, жёлтый = 10×, or `—` for set 1).
4. The `group_id` field gives the full compound key, e.g. `S2-ch17-N1-b` = set 2, channel 17, neutral medium, replicate 1, zone белый.

**Semantics of the key fields (researcher-confirmed 2026-06-09):**

| Journal field | Meaning |
|---|---|
| `channel 0` | Control — no field exposure |
| `channel 17` | Hyperbolic field configuration CH17 (was "unknown" per protocol; observed highest density) |
| `channel 19` | Hyperbolic field configuration CH19 — "acceleration" |
| `channel 21` | Hyperbolic field configuration CH21 — "deceleration" |
| `exposure N` | Neutral growth medium (нейтральный раствор) |
| `exposure P` | Nutrient growth medium (питательный раствор) |
| `set 1 / 2 / 3` | Experiment cycle (biological replicate batch) |
| `zone белый` | 100× magnification (white objective ring) |
| `zone жёлтый` | 10× magnification (yellow objective ring) |
| `zone —` | Set 001 only — no magnification split recorded |

**Known anomalies in the image sequence (from the verified journal):**

- `IMG_4819`: struck-through in journal (treat as cancelled; 4820 is the effective first of S1-ch0-P1)
- `IMG_4847`: struck-through as block divider; file present on disk but outside any mapped group
- `IMG_4857`: absent on disk (skip in S1-ch17-P2)
- `IMG_4868`: present on disk but unlogged (S1-ch17-P2 journals skip it)
- `IMG_4941`: absent on disk (skip in S1-ch21-P1, disk-confirmed)
- `IMG_4971`: absent (skip in S1-ch21-N2 per journal)
- `IMG_4988`: cancelled/struck in journal; PNG file on disk is microscopy, not a field photo
- `IMG_5090`, `IMG_5142`, `IMG_5657`: present on disk, documented unlogged single frames

---

## Data Directory Tree

```
Hyperbolic_Field_SaccharomycesCerevisiae_Study/
├── en/
│   └── README.md                   (this file — English data-browse hub)
├── ru/
│   └── README.md                   (Russian mirror)
├── data/
│   ├── README.md                   (bilingual data hub)
│   ├── photos/
│   │   ├── README.md               (per-image inventory, 990 entries)
│   │   ├── manifest.json           (machine-readable metadata)
│   │   ├── journal-mapping.csv   (authoritative IMG → group mapping)
│   │   ├── journal-mapping.json  (same, JSON format)
│   │   ├── journal-note.txt      (researcher journal verbatim)
│   │   ├── original/               (iPhone-native HEIC + PNG, 990 files)
│   │   └── jpg/                    (JPEG previews, 972 files)
│   ├── control-01/ … control-03/   (analysis bins — empty, pending attribution)
│   ├── sample-ch17/                (analysis bin — CH17 samples)
│   ├── sample-ch19/                (analysis bin — CH19 samples)
│   ├── sample-ch21/                (analysis bin — CH21 samples)
│   ├── sample-ch17-19/             (analysis bin — combined CH17+CH19)
│   ├── microscopy/
│   │   └── staining/               (methylene blue staining photos)
│   └── equipment/                  (emitter and sensor setup photos)
├── results/
│   ├── SEMANTICS_CONFIRMED.md      (researcher-confirmed label semantics, 2026-06-09)
│   ├── cv_analysis/
│   │   ├── DENSITY_SUMMARY.md      (CV density analysis summary)
│   │   ├── occupancy_full.csv / .json
│   │   ├── white_counts.csv / .json
│   │   └── white_counts_morpho.csv / .json
│   └── llm_blind/
│       ├── blind_run_1.json
│       └── blind_run_2.json
├── reports/
│   └── 2026-06-09_density-analysis/
│       ├── report_en.md            (full English density analysis report)
│       ├── report_ru.md            (full Russian density analysis report)
│       └── charts/                 (analysis charts)
├── protocols/                      (experiment protocols)
├── charts/                         (mermaid diagrams)
└── scripts/                        (CV pipeline scripts, TBD)
```

---

## Reports

| Report | Date | Description |
|---|---|---|
| [Density analysis (CV + LLM)](../reports/2026-06-09_density-analysis/report_en.md) | 2026-06-09 | Triangulated CV cell-count + occupancy + blind LLM scoring across 972 fields; CH17 / CH21 / CH19 vs control |

---

## Preliminary Key Findings (2026-06-09)

Analysis of the first imaging batch (972 microscopy fields, cycles 001–003) using three independent methods
(CV cell count at 100×, CV occupancy, blind LLM scoring) produced a consistent directional signal:

| Channel | Cell count at 100× | vs control | Occupancy rank (cycles 2–3) |
|:---:|:---:|:---:|:---:|
| CH0 (control) | 112 | — | mid |
| **CH17** | **205** | **+83%** | **1st (densest, every method)** |
| CH19 | 118 | +5% | 2nd |
| **CH21** | **88** | **−21%** | **4th (below control, every method)** |

CH19 is not a null result: its effect is kinetic/morphological — cells are ~7.6% smaller in area (p ≈ 6e-5 descriptive). **CH19's pre-registered role (hypothesis) is to accelerate division rate / dynamics, NOT increase biomass or cell count** (count ≈ control is the expected outcome; the count increase is CH17). On this static endpoint batch cells are ~7.6% smaller in area but not more elongated and budding is flat — the division-rate hypothesis needs time-lapse / OD600 follow-up (see report §9).

Per-field method agreement (Spearman): CV-count ↔ occupancy ρ = 0.88; occupancy ↔ LLM ρ = 0.89; CV-count ↔ LLM ρ = 0.81.

> **Caveat:** Preliminary — only 3 cycles; cycle 1 disagrees with ordering; p-values are descriptive only
> (pseudoreplication); no scale bar. Evidence is cross-method / cross-cycle consistency, not significance.
> Needs ≥5 independent cycles for a confirmatory claim.

---

## Experiment Protocol Sequence

General sequence for each experiment cycle (batch):

1. **Sample preparation** — dry yeast (*S. cerevisiae*, Dr. Oetker 7g, batch L329 M68) dissolved in growth medium (N or P)
2. **Allocation** — distribution into sample containers (control CH0 + field-exposed CH17 / CH19 / CH21)
3. **Irradiation** — 80 minutes (1h 20m); 6-node emitter, 60 W avg / 144 W peak, clean sine wave; complete darkness during irradiation
4. **Microscopy** — light microscope, strong LED illumination; phone-through-eyepiece imaging at 100× (white ring) and 10× (yellow ring) objectives
5. **Photo logging** — iPhone camera roll, sequential IMG_XXXX numbers; documented in researcher journal (pages A/B for cycle 1, page C table for cycles 2–3)
6. **Documentation** — DHT11 temperature sensors (next to each sample), photoresistors for light monitoring

> **No viability stain in this batch:** the first imaging batch (990 fields, 2026-04-19 to 2026-04-22) was captured
> without methylene blue staining (researcher-confirmed). The blue cast in images is medium/illumination, not dye.
> This batch reports **cell density only**. Methylene blue viability staining is part of the registered protocol
> for future batches.

---

## Researcher-Confirmed Semantics

Source: `../results/SEMANTICS_CONFIRMED.md` (researcher disclosure, 2026-06-09).

- **N** = neutral solution (growth medium)
- **P** = nutrient solution (growth medium)
- **Sets 001 / 002 / 003** = experiment cycles (biological replicates over time)
- **Channel 0** = control (no field)
- **Channel 17 / 19 / 21** = hyperbolic field configurations
- **Zone белый** = 100× magnification (white objective ring)
- **Zone жёлтый** = 10× magnification (yellow objective ring)
- **Group S2-ch0-P1** = failed group (sample spilled / absent); journal dashes are correct; 0 photos

---

## Related Studies

**Companion study — Hyperbolic Field Blood Plasma Study**

The Blood Plasma Study is the direct predecessor to this repo and the source of the channel-direction precedents used in H3. It tested the same CH17/CH19/CH21 channel configuration on human blood plasma coagulation. CH19 produced fast clot formation + lysis (time-acceleration behaviour); CH21 produced dense, slow clot (time-deceleration). These observations grounded the directional hypotheses carried over to the yeast system.

- GitHub: [Hyperbolic_Field_BloodPlasma_Study](https://github.com/AdvancedScientificResearchProjects/Hyperbolic_Field_BloodPlasma_Study)
- OSF: [osf.io/8q42f](https://osf.io/8q42f)
- DOI: [10.17605/OSF.IO/GWA9E](https://doi.org/10.17605/OSF.IO/GWA9E)

---

## License

CC-BY-NC-ND 4.0 International

© 2026 Advanced Scientific Research Projects LLP (ASRP). All rights reserved.

Organization: Advanced Scientific Research Projects LLP  
Address: Komarova St. 37, Apt 56, Baikonur, 468320, Republic of Kazakhstan  
Website: [asrp.tech](https://asrp.tech) · Email: info@asrp.tech
