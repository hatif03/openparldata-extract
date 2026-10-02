# OpenParlData challenge brief (working notes)

Synced from study repo `apertus/track-2a/openparldata/`. Update after the **2 Oct** provider deep dive (Luma — watch Discord).

## Official

| Resource | URL |
| --- | --- |
| Platform | https://openparldata.ch/home |
| API docs | https://api.openparldata.ch/documentation |
| OpenAPI | https://api.openparldata.ch/openapi.json |
| BFH project | https://www.bfh.ch/en/research/research-projects/2025-251-431-560/ |
| Glue / eCH context | https://www.glue.ch/en/2025/05/12/56658/ |

## Standards & code

| Resource | Why |
| --- | --- |
| [gitlab.com/opendata.ch/openparldatach](https://gitlab.com/opendata.ch/openparldatach) | Current OpenParlData codebase |
| [swiss/political-affairs-ech-group](https://github.com/swiss/political-affairs-ech-group) | eCH-0292–0297; **eCH-0295** target |
| [ech.ch — Politische Geschäfte](https://ech.ch/de/der-verein/fachgruppen/politische-geschaefte) | Standard status |
| [malkreide/parlament-mcp](https://github.com/malkreide/parlament-mcp) | API already exposes some document **text**; gap is **structure** |
| [docling-project/docling](https://github.com/docling-project/docling) | Layout-aware PDF (IBM Research Zurich) |
| [VikParuchuri/marker](https://github.com/VikParuchuri/marker) | PDF → Markdown |
| [technologiestiftung/parla-document-processor](https://github.com/technologiestiftung/parla-document-processor) | Parliamentary PDF pattern (Berlin) |

## Apertus role (do not skip layout tools)

1. **Docling/Marker** for layout — avoid asking the LLM to OCR 80-page scans from scratch.  
2. **Apertus 1.5** maps messy Markdown into **schema-valid JSON** (long context; thinking only for field disambiguation, separate from strict JSON pass if needed).  
3. **Optional:** page **images** to Apertus 1.5 multimodal for failed scan pages.

Engineering parallels GemeindeSim: filled JSON example, Pydantic validation, repair pass, no parallel tool fan-out in one completion.

## Learn path

1. Swagger: list bodies, one affair, documents.  
2. Skim eCH-0295 in the GitHub group repo.  
3. `pip install docling` on one public PDF.  
4. Read parlament-mcp — what the API already returns.  
5. After 2 Oct: confirm gold PDFs, languages, scan/digital mix, exact judging rubric.

## Clone order (first week)

1. API: bodies → affair → docs  
2. Draft JSON schema (even if replaced on 2 Oct)  
3. One PDF through Docling  
4. One Apertus mapping call with `response_format: json_object`
