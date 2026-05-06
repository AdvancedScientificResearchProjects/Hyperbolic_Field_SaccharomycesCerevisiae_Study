# Photos / Фотографии

Flat photo set for the *Saccharomyces cerevisiae* hyperbolic-field study. Photos are stored as iPhone-native HEIC/PNG in `original/` with JPEG previews in `jpg/`. Per-photo metadata is in `manifest.json`.

Плоский набор фотографий по исследованию влияния гиперболических полей на *Saccharomyces cerevisiae*. Фотографии хранятся как iPhone-native HEIC/PNG в `original/` с JPEG-превью в `jpg/`. Метаданные по каждой фотографии — в `manifest.json`.

---

## Summary / Сводка

| Field / Поле | Value / Значение |
|---|---|
| Total photos / Всего фото | 198 |
| HEIC | 180 |
| JPEG | 0 |
| PNG (microscopy / микроскопия) | 18 |
| Date range / Диапазон дат | 2026-04-19 — 2026-04-22 |
| Photos with `comparison_layout` / С пространственной разметкой | 0 |
| Photos with `group_label` / С меткой группы | 0 (pending researcher / ожидается) |

---

## Schema / Схема

Each entry in `manifest.json`:
Каждая запись в `manifest.json`:

- **`id`** — sequential 1..N / порядковый 1..N
- **`filename`** — file under `original/` (HEIC/PNG) or `jpg/` (JPEG) / файл в `original/` (HEIC/PNG) или `jpg/` (JPEG)
- **`format`** — `HEIC` / `JPEG` / `PNG`
- **`date_observed`** — `YYYY-MM-DD`, the date of the observation / дата наблюдения
- **`jpg_preview`** — JPEG preview filename in `jpg/`, when available / имя JPEG-превью в `jpg/`, если есть
- **`subject`** — biological subject / биологический объект (`Saccharomyces cerevisiae`)
- **`group_label`** — `irradiated` / `control` / `null` (single-sample frames; null until researcher attribution / для одно-образцовых кадров; null до атрибуции руководителем)
- **`comparison_layout`** — spatial layout for multi-sample frames, e.g. `left=irradiated` / пространственная разметка для много-образцовых кадров, например `left=irradiated`
- **`notes`** — short visual note (optional) / короткое визуальное примечание (опционально)

`group_label` and `comparison_layout` are mutually exclusive. / `group_label` и `comparison_layout` взаимоисключающие.

---

## Inventory / Список

| # | File / Файл | Date / Дата | Format / Формат | Group / Группа | Comparison / Разметка | Preview / Превью |
|---|---|---|---|---|---|---|
| 1 | `original/IMG_4801.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4801.jpg) |
| 2 | `original/IMG_4802.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4802.jpg) |
| 3 | `original/IMG_4803.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4803.jpg) |
| 4 | `original/IMG_4804.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4804.jpg) |
| 5 | `original/IMG_4805.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4805.jpg) |
| 6 | `original/IMG_4806.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4806.jpg) |
| 7 | `original/IMG_4807.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4807.jpg) |
| 8 | `original/IMG_4808.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4808.jpg) |
| 9 | `original/IMG_4809.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4809.jpg) |
| 10 | `original/IMG_4810.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4810.jpg) |
| 11 | `original/IMG_4811.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4811.jpg) |
| 12 | `original/IMG_4812.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4812.jpg) |
| 13 | `original/IMG_4813.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4813.jpg) |
| 14 | `original/IMG_4814.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4814.jpg) |
| 15 | `original/IMG_4815.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4815.jpg) |
| 16 | `original/IMG_4816.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4816.jpg) |
| 17 | `original/IMG_4817.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4817.jpg) |
| 18 | `original/IMG_4818.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4818.jpg) |
| 19 | `original/IMG_4820.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4820.jpg) |
| 20 | `original/IMG_4821.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4821.jpg) |
| 21 | `original/IMG_4822.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4822.jpg) |
| 22 | `original/IMG_4823.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4823.jpg) |
| 23 | `original/IMG_4824.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4824.jpg) |
| 24 | `original/IMG_4825.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4825.jpg) |
| 25 | `original/IMG_4826.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4826.jpg) |
| 26 | `original/IMG_4827.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4827.jpg) |
| 27 | `original/IMG_4828.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4828.jpg) |
| 28 | `original/IMG_4829.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4829.jpg) |
| 29 | `original/IMG_4830.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4830.jpg) |
| 30 | `original/IMG_4831.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4831.jpg) |
| 31 | `original/IMG_4832.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4832.jpg) |
| 32 | `original/IMG_4833.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4833.jpg) |
| 33 | `original/IMG_4834.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4834.jpg) |
| 34 | `original/IMG_4835.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4835.jpg) |
| 35 | `original/IMG_4836.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4836.jpg) |
| 36 | `original/IMG_4837.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4837.jpg) |
| 37 | `original/IMG_4838.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4838.jpg) |
| 38 | `original/IMG_4839.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4839.jpg) |
| 39 | `original/IMG_4840.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4840.jpg) |
| 40 | `original/IMG_4841.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4841.jpg) |
| 41 | `original/IMG_4842.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4842.jpg) |
| 42 | `original/IMG_4844.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4844.jpg) |
| 43 | `original/IMG_4845.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4845.jpg) |
| 44 | `original/IMG_4846.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4846.jpg) |
| 45 | `original/IMG_4847.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4847.jpg) |
| 46 | `original/IMG_4848.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4848.jpg) |
| 47 | `original/IMG_4849.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4849.jpg) |
| 48 | `original/IMG_4850.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4850.jpg) |
| 49 | `original/IMG_4851.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4851.jpg) |
| 50 | `original/IMG_4852.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4852.jpg) |
| 51 | `original/IMG_4853.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4853.jpg) |
| 52 | `original/IMG_4854.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4854.jpg) |
| 53 | `original/IMG_4855.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4855.jpg) |
| 54 | `original/IMG_4856.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4856.jpg) |
| 55 | `original/IMG_4858.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4858.jpg) |
| 56 | `original/IMG_4859.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4859.jpg) |
| 57 | `original/IMG_4860.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4860.jpg) |
| 58 | `original/IMG_4861.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4861.jpg) |
| 59 | `original/IMG_4862.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4862.jpg) |
| 60 | `original/IMG_4863.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4863.jpg) |
| 61 | `original/IMG_4864.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4864.jpg) |
| 62 | `original/IMG_4865.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4865.jpg) |
| 63 | `original/IMG_4866.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4866.jpg) |
| 64 | `original/IMG_4867.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4867.jpg) |
| 65 | `original/IMG_4868.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4868.jpg) |
| 66 | `original/IMG_4869.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4869.jpg) |
| 67 | `original/IMG_4870.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4870.jpg) |
| 68 | `original/IMG_4871.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4871.jpg) |
| 69 | `original/IMG_4872.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4872.jpg) |
| 70 | `original/IMG_4873.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4873.jpg) |
| 71 | `original/IMG_4874.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4874.jpg) |
| 72 | `original/IMG_4875.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4875.jpg) |
| 73 | `original/IMG_4876.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4876.jpg) |
| 74 | `original/IMG_4878.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4878.jpg) |
| 75 | `original/IMG_4879.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4879.jpg) |
| 76 | `original/IMG_4880.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4880.jpg) |
| 77 | `original/IMG_4881.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4881.jpg) |
| 78 | `original/IMG_4882.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4882.jpg) |
| 79 | `original/IMG_4883.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4883.jpg) |
| 80 | `original/IMG_4884.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4884.jpg) |
| 81 | `original/IMG_4885.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4885.jpg) |
| 82 | `original/IMG_4886.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4886.jpg) |
| 83 | `original/IMG_4887.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4887.jpg) |
| 84 | `original/IMG_4888.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4888.jpg) |
| 85 | `original/IMG_4889.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4889.jpg) |
| 86 | `original/IMG_4890.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4890.jpg) |
| 87 | `original/IMG_4891.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4891.jpg) |
| 88 | `original/IMG_4892.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4892.jpg) |
| 89 | `original/IMG_4893.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4893.jpg) |
| 90 | `original/IMG_4894.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4894.jpg) |
| 91 | `original/IMG_4895.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4895.jpg) |
| 92 | `original/IMG_4896.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4896.jpg) |
| 93 | `original/IMG_4897.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4897.jpg) |
| 94 | `original/IMG_4898.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4898.jpg) |
| 95 | `original/IMG_4899.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4899.jpg) |
| 96 | `original/IMG_4900.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4900.jpg) |
| 97 | `original/IMG_4901.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4901.jpg) |
| 98 | `original/IMG_4902.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4902.jpg) |
| 99 | `original/IMG_4903.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4903.jpg) |
| 100 | `original/IMG_4904.HEIC` | 2026-04-19 | HEIC | — | — | [↗](jpg/IMG_4904.jpg) |
| 101 | `original/IMG_4905.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4905.jpg) |
| 102 | `original/IMG_4906.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4906.jpg) |
| 103 | `original/IMG_4907.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4907.jpg) |
| 104 | `original/IMG_4908.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4908.jpg) |
| 105 | `original/IMG_4909.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4909.jpg) |
| 106 | `original/IMG_4910.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4910.jpg) |
| 107 | `original/IMG_4911.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4911.jpg) |
| 108 | `original/IMG_4912.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4912.jpg) |
| 109 | `original/IMG_4913.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4913.jpg) |
| 110 | `original/IMG_4914.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4914.jpg) |
| 111 | `original/IMG_4915.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4915.jpg) |
| 112 | `original/IMG_4916.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4916.jpg) |
| 113 | `original/IMG_4917.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4917.jpg) |
| 114 | `original/IMG_4918.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4918.jpg) |
| 115 | `original/IMG_4919.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4919.jpg) |
| 116 | `original/IMG_4920.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4920.jpg) |
| 117 | `original/IMG_4921.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4921.jpg) |
| 118 | `original/IMG_4922.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4922.jpg) |
| 119 | `original/IMG_4923.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4923.jpg) |
| 120 | `original/IMG_4924.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4924.jpg) |
| 121 | `original/IMG_4925.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4925.jpg) |
| 122 | `original/IMG_4926.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4926.jpg) |
| 123 | `original/IMG_4927.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4927.jpg) |
| 124 | `original/IMG_4928.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4928.jpg) |
| 125 | `original/IMG_4929.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4929.jpg) |
| 126 | `original/IMG_4930.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4930.jpg) |
| 127 | `original/IMG_4931.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4931.jpg) |
| 128 | `original/IMG_4932.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4932.jpg) |
| 129 | `original/IMG_4933.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4933.jpg) |
| 130 | `original/IMG_4934.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4934.jpg) |
| 131 | `original/IMG_4935.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4935.jpg) |
| 132 | `original/IMG_4936.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4936.jpg) |
| 133 | `original/IMG_4937.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4937.jpg) |
| 134 | `original/IMG_4938.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4938.jpg) |
| 135 | `original/IMG_4939.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4939.jpg) |
| 136 | `original/IMG_4940.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4940.jpg) |
| 137 | `original/IMG_4942.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4942.jpg) |
| 138 | `original/IMG_4943.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4943.jpg) |
| 139 | `original/IMG_4944.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4944.jpg) |
| 140 | `original/IMG_4945.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4945.jpg) |
| 141 | `original/IMG_4946.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4946.jpg) |
| 142 | `original/IMG_4947.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4947.jpg) |
| 143 | `original/IMG_4948.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4948.jpg) |
| 144 | `original/IMG_4949.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4949.jpg) |
| 145 | `original/IMG_4950.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4950.jpg) |
| 146 | `original/IMG_4951.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4951.jpg) |
| 147 | `original/IMG_4952.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4952.jpg) |
| 148 | `original/IMG_4953.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4953.jpg) |
| 149 | `original/IMG_4954.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4954.jpg) |
| 150 | `original/IMG_4955.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4955.jpg) |
| 151 | `original/IMG_4956.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4956.jpg) |
| 152 | `original/IMG_4957.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4957.jpg) |
| 153 | `original/IMG_4958.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4958.jpg) |
| 154 | `original/IMG_4959.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4959.jpg) |
| 155 | `original/IMG_4960.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4960.jpg) |
| 156 | `original/IMG_4961.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4961.jpg) |
| 157 | `original/IMG_4962.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4962.jpg) |
| 158 | `original/IMG_4963.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4963.jpg) |
| 159 | `original/IMG_4964.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4964.jpg) |
| 160 | `original/IMG_4965.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4965.jpg) |
| 161 | `original/IMG_4966.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4966.jpg) |
| 162 | `original/IMG_4967.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4967.jpg) |
| 163 | `original/IMG_4968.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4968.jpg) |
| 164 | `original/IMG_4969.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4969.jpg) |
| 165 | `original/IMG_4970.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4970.jpg) |
| 166 | `original/IMG_4972.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4972.jpg) |
| 167 | `original/IMG_4973.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4973.jpg) |
| 168 | `original/IMG_4974.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4974.jpg) |
| 169 | `original/IMG_4975.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4975.jpg) |
| 170 | `original/IMG_4976.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4976.jpg) |
| 171 | `original/IMG_4977.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4977.jpg) |
| 172 | `original/IMG_4978.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4978.jpg) |
| 173 | `original/IMG_4979.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4979.jpg) |
| 174 | `original/IMG_4980.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4980.jpg) |
| 175 | `original/IMG_4981.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4981.jpg) |
| 176 | `original/IMG_4983.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4983.jpg) |
| 177 | `original/IMG_4984.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4984.jpg) |
| 178 | `original/IMG_4985.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4985.jpg) |
| 179 | `original/IMG_4986.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4986.jpg) |
| 180 | `original/IMG_4987.HEIC` | 2026-04-22 | HEIC | — | — | [↗](jpg/IMG_4987.jpg) |
| 181 | `original/IMG_4988.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4988.PNG) |
| 182 | `original/IMG_4989.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4989.PNG) |
| 183 | `original/IMG_4990.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4990.PNG) |
| 184 | `original/IMG_4991.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4991.PNG) |
| 185 | `original/IMG_4992.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4992.PNG) |
| 186 | `original/IMG_4993.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4993.PNG) |
| 187 | `original/IMG_4994.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4994.PNG) |
| 188 | `original/IMG_4995.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4995.PNG) |
| 189 | `original/IMG_4996.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4996.PNG) |
| 190 | `original/IMG_4997.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4997.PNG) |
| 191 | `original/IMG_4998.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4998.PNG) |
| 192 | `original/IMG_4999.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_4999.PNG) |
| 193 | `original/IMG_5001.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_5001.PNG) |
| 194 | `original/IMG_5002.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_5002.PNG) |
| 195 | `original/IMG_5003.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_5003.PNG) |
| 196 | `original/IMG_5004.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_5004.PNG) |
| 197 | `original/IMG_5006.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_5006.PNG) |
| 198 | `original/IMG_5007.PNG` | 2026-04-22 | PNG | — | — | [↗](original/IMG_5007.PNG) |

---

## What this set does NOT claim / Чего этот набор НЕ утверждает

- **EN:** Does NOT report numerical measurements (CFU counts, optical density, area-under-curve). Quantitative analysis is produced separately.
- **EN:** Does NOT attribute photos to specific samples / controls / channels. That attribution is a researcher-disclosure step.
- **EN:** Does NOT validate the photographs as a calibrated assay. They are observational records pending researcher analysis.
- **RU:** НЕ приводит численные измерения (КОЕ, оптическая плотность, площадь под кривой). Количественный анализ производится отдельно.
- **RU:** НЕ привязывает фотографии к конкретным образцам / контролям / каналам. Эта атрибуция — шаг раскрытия со стороны руководителя.
- **RU:** НЕ утверждает, что фотографии — это калиброванный аналитический метод. Это наблюдательные записи, ожидающие анализа руководителя.
