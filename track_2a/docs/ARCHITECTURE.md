# Pipeline architecture (draft)

```text
PDF (affair document)
        │
        ▼
┌───────────────────┐
│ Docling / Marker  │  layout, tables, reading order
└─────────┬─────────┘
          │ Markdown or JSON blocks + optional page images
          ▼
┌───────────────────┐
│ Chunk + retrieve  │  map sections → schema field hints (code)
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Apertus 1.5       │  json mode → eCH-0295 / OpenParlData shape
│ (70B default)     │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Validate          │  OpenAPI / JSON Schema / Pydantic
└─────────┬─────────┘
          │
          ▼
   OpenParlData-compatible JSON
```

## Planned `src/` modules

| Module | Role |
| --- | --- |
| `opd_extract/ingest.py` | Load PDF from `data/` or URL list |
| `opd_extract/layout.py` | Docling/Marker wrapper |
| `opd_extract/schema.py` | Target affair model (eCH-0295 subset) |
| `opd_extract/map_llm.py` | Apertus client + example-instance prompts |
| `opd_extract/validate.py` | Schema + optional OpenAPI check |
| `opd_extract/cli.py` | `python -m opd_extract path/to.pdf` |
| `opd_extract/eval/` | Field-level F1 vs gold JSON (when available) |

## Failure modes to engineer around

| Issue | Mitigation |
| --- | --- |
| Bad table reading | Docling first; vision pass on failed pages only |
| Hallucinated fields | Closed schema; reject unknown keys |
| Long documents | Chunk by heading; merge with code, not one blind 200k paste |
| DE/FR/IT mix | Language tag per block; map per official language rules |
| Apertus JSON drops keys | Filled example + repair call (see GemeindeSim probe) |
