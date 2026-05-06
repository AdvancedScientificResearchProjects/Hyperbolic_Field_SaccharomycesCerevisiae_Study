# Yeast Data Hub / Хаб данных по дрожжам

**Hyperbolic Field *Saccharomyces cerevisiae* Study / Исследование Влияния Гиперболических Полей на *Saccharomyces cerevisiae***

---

## Quick Navigation / Быстрая навигация

| Section / Раздел | Description / Описание |
|---|---|
| [Overview](#overview--обзор) | Dataset layout / Структура набора |
| [Photos](#photos--фотографии) | Flat photo set + manifest / Плоский набор + манифест |
| [Analysis bins](#analysis-bins--аналитические-корзины) | Empty placeholders awaiting attribution / Пустые корзины ожидают атрибуции |
| [Schema](#schema--схема) | Layout reference / Справка по структуре |

---

## Overview / Обзор

### EN

This `data/` directory holds the observational image set for the *Saccharomyces cerevisiae* hyperbolic-field study and the protocol-aligned bins that will receive a researcher-driven attribution of those images at a later analysis stage. The set is layered:

- **`photos/`** — flat photo collection with one manifest entry per image (HEIC/PNG originals + JPEG previews/JPEG-only deliveries). Each photo carries `subject`, `date_observed`, optional `group_label` (single-sample frames) or `comparison_layout` (multi-sample frames), and free-form `notes`.
- **`control-NN/`, `sample-chXX/`, `sample-chXX-YY/`, `microscopy/`, `equipment/`** — protocol-v8.3-aligned analysis bins. They are present as empty placeholders. Photos move (or are linked) into the appropriate bin once the research lead discloses which photo belongs to which sample / control / channel / instrument.

The two surfaces are complementary, not redundant: `photos/` is the canonical raw observation set; the bins are the analytical projection. A photo may appear by hard link or symlink in both surfaces once attributed.

### RU

Каталог `data/` содержит набор наблюдательных изображений по исследованию влияния гиперболических полей на *Saccharomyces cerevisiae* и протокол-выровненные корзины, которые получат атрибуцию этих изображений руководителем на более поздней стадии анализа. Структура двухуровневая:

- **`photos/`** — плоская коллекция фото с одной записью манифеста на изображение (HEIC/PNG-оригиналы + JPEG-превью/JPEG-only поставки). Каждая фотография имеет `subject`, `date_observed`, опционально `group_label` (одно-образцовые кадры) или `comparison_layout` (много-образцовые кадры), и свободные `notes`.
- **`control-NN/`, `sample-chXX/`, `sample-chXX-YY/`, `microscopy/`, `equipment/`** — корзины анализа выровненные с протоколом v8.3. Сейчас они пустые плейсхолдеры. Фото переносятся (или линкуются) в соответствующую корзину после раскрытия руководителем какое фото принадлежит какому образцу / контролю / каналу / инструменту.

Две поверхности взаимно дополняющие: `photos/` — каноничный сырой набор наблюдений; корзины — аналитическая проекция. Одна фотография может присутствовать в обеих через жёсткую ссылку / симлинк после атрибуции.

---

## Photos / Фотографии

| Field / Поле | Value / Значение |
|---|---|
| Total / Всего | 198 |
| HEIC | 180 |
| PNG (microscopy / микроскопия) | 18 |
| Date range / Диапазон дат | 2026-04-19 — 2026-04-22 |
| With `comparison_layout` / С пространственной разметкой | 0 |
| With `group_label` / С меткой группы | 0 (pending researcher / ожидается) |

→ See [`photos/README.md`](photos/README.md) for the per-image inventory and [`photos/manifest.json`](photos/manifest.json) for machine-readable metadata.

→ См. [`photos/README.md`](photos/README.md) — поэлементный список, и [`photos/manifest.json`](photos/manifest.json) — машинно-читаемые метаданные.

---

## Analysis bins / Аналитические корзины

These directories follow the protocol-v8.3 layout. They are populated when the research lead attributes images from `photos/` to specific samples / controls / channels / instruments.

Эти каталоги соответствуют разметке протокола v8.3. Заполняются, когда руководитель привязывает изображения из `photos/` к конкретным образцам / контролям / каналам / инструментам.

| Bin / Корзина | Status / Статус |
|---|---|
| `control-01/` `control-02/` `control-03/` | Empty placeholder — pending / Пустой плейсхолдер — ожидание |
| `sample-ch17/` `sample-ch17-19/` `sample-ch19/` `sample-ch21/` | Empty placeholder — pending / Пустой плейсхолдер — ожидание |
| `microscopy/` | Empty placeholder — pending / Пустой плейсхолдер — ожидание |
| `equipment/` | Empty placeholder — pending / Пустой плейсхолдер — ожидание |

---

## Schema / Схема

```
data/
├── README.md                      (this file / этот файл)
├── photos/
│   ├── README.md                  (per-image inventory table / поэлементная таблица)
│   ├── manifest.json              (machine-readable metadata / машинно-читаемые метаданные)
│   ├── original/                  (iPhone-native HEIC + PNG / iPhone-native HEIC + PNG)
│   └── jpg/                       (JPEG previews / JPEG-only / JPEG-превью / JPEG-only)
├── control-NN/                    (analysis bins, empty until attribution / корзины анализа)
│   ├── metadata.json
│   └── photos/
├── sample-chXX[/-YY]/
├── microscopy/
└── equipment/
```

---

## What this hub does NOT claim / Чего этот хаб НЕ утверждает

- **EN:** Does NOT report numerical measurements (CFU counts, optical density, area-under-curve). Quantitative analysis is produced separately.
- **EN:** Does NOT attribute photos to specific samples / controls / channels. That attribution is a researcher-disclosure step.
- **EN:** Does NOT validate the photographs as a calibrated assay. They are observational records pending researcher analysis.
- **RU:** НЕ приводит численные измерения (КОЕ, оптическая плотность, площадь под кривой). Количественный анализ производится отдельно.
- **RU:** НЕ привязывает фотографии к конкретным образцам / контролям / каналам. Эта атрибуция — шаг раскрытия со стороны руководителя.
- **RU:** НЕ утверждает, что фотографии — это калиброванный аналитический метод. Это наблюдательные записи, ожидающие анализа руководителя.
