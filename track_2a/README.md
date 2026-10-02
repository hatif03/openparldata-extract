# OpenParlData — Extracting Parliamentary Affairs from PDFs

**Hack Apertus Track 2A** · Partner: **OpenParlData / BFH** · Christian Gutknecht (OpenParlData, Glue, eCH Political Affairs)

Swiss parliaments publish **affaires** (Vorstösse, Berichte, Beschlüsse) as inconsistent PDFs. This project extracts text and maps it into **one common structure** so it can join the [OpenParlData API](https://api.openparldata.ch/documentation) (~78 bodies today, incompatible layouts).

## Problem (two layers)

1. **Layout / OCR** — reading order, tables, scans vs born-digital ([Docling](https://github.com/docling-project/docling), [Marker](https://github.com/VikParuchuri/marker), etc.)
2. **Schema mapping** — title, body, dates, actors, Beschluss, language → **eCH-0295** / OpenParlData JSON

**Apertus 1.5:** long-context cleanup into valid JSON; optional **page images** for scans Docling misses. Do not invent fields outside the target schema.

## Prototype target (16 days)

- 5–10 real affair PDFs (OpenParlData doc links or cantonal sites)  
- Docling or Marker → intermediate Markdown/JSON  
- Apertus fills the target schema → validate against OpenAPI / eCH-0295  
- Score **table/header fidelity**, not raw OCR alone  

## Run it

Keep `track_2a/` unchanged (template rule). From **repository root**:

```bash
make run
```

Docker + `LLM_*` env vars (see `.env.example`). Stub until pipeline is implemented.

## Data

`data/` ≤ **100 MB**. Store small samples + metadata; link to sources in the technical report.

## Submission

| Item | Link |
| --- | --- |
| Form | http://hackapertus.ch/online-hack/submissions |
| Challenge details | https://hackapertus.notion.site/getting-started-guide-onlinehack |
| Judging | Per challenge in Notion (see `docs/HACKATHON.md`) |

**Deadline:** 16 October 2026, 12:00 CEST.

## Docs in this repo

- [docs/CHALLENGE.md](docs/CHALLENGE.md) — resources, learn path, Apertus angle  
- [docs/HACKATHON.md](docs/HACKATHON.md) — deadlines, checklist  
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — pipeline sketch  
- [technical_report.md](technical_report.md) — submission write-up  

## Support

Discord: https://discord.gg/hack-apertus · hello@hackapertus.ch
