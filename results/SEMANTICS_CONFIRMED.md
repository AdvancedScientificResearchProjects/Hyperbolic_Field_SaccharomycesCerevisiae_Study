# Confirmed data semantics (researcher-confirmed, 2026-06-09)

Source: researcher confirmation, 2026-06-09; cross-checked against the microscope-objectives photograph (SEMANTICS_objectives_photo.jpg).

| Journal label | Meaning |
|---|---|
| **N** | Нейтральный раствор / neutral solution (growth medium) |
| **P** | Питательный раствор / nutrient solution (growth medium) |
| **set 001 / 002 / 003** | Experiment CYCLE (batch): 001 = first batch irradiated across all channels; 002 = second; 003 = third. → biological replicates over time. |
| **channel 0** | CONTROL (no field) — user-confirmed earlier |
| **channel 17 / 19 / 21** | Hyperbolic-field configurations (CH19=accel, CH21=decel, CH17 was "unknown" per protocol) |
| **zone белый** | Microscope magnification 100× (white objective ring) |
| **zone жёлтый** | Microscope magnification 10× (yellow objective ring) |
| **2-0-P1** | Failed group — sample spilled / absent (empty; the journal dashes are correct) |
| Source archive | Verified byte-identical (HEIC checksum match) to the analyzed image set. |

## Implications for analysis
- "Field vs control" axis = CHANNEL (0 vs 17/19/21). N/P is a medium co-factor; magnification (white/yellow) is an imaging factor.
- Compare density WITHIN magnification only (10×↔10×, 100×↔100×); cell COUNT is meaningless at 10× (confluent lawn) → use occupancy/texture density there.
- Sets 1/2/3 = experiment cycles = replicate unit for proper (non-pseudoreplicated) stats.
- NO viability stain: the blue cast is medium/illumination, zones are magnification, not staining → viability analysis is not applicable.
