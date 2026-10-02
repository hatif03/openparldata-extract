# Technical report — OpenParlData Extract

A deeper write-up than the README: what you built, how it works, and what the
numbers say. Also check the specific submission requirements for the **OpenParlData**
challenge in the [getting-started guide](https://hackapertus.notion.site/getting-started-guide-onlinehack).

- **Track:** Track 2A — OpenParlData (parliamentary PDFs → one structure)
- **Event:** Hack Apertus online stage, October 2026
- **Team:** _TBD_
- **Demo:** _TBD_

## 1. Summary

_Swiss parliamentary affair PDFs are converted with a layout tool (Docling/Marker), then Apertus 1.5-70B maps the intermediate representation into schema-valid JSON aligned with eCH-0295 / OpenParlData. Headline metrics: TBD (field accuracy vs gold, table fidelity)._

## 2. Architecture

Components, data flow, and where each one runs. Put diagrams in `docs/` and
reference them here.

## 3. Use of Apertus

- **Model:** `apertus-v1.5-70b` on hackathon endpoint; weights `swiss-ai/Apertus-v1.5-70B`
- **How it is used:** inference — structured JSON mapping from layout output; optional multimodal page images for failed OCR regions
- **Where it runs:** `https://hackapertus.livemap.sh/v1` (demo); sovereign/on-prem vLLM for production story
- **Not used for:** raw OCR of full scans when Docling/Marker suffices (per challenge design)

Prompts, adapters, quantisation, serving stack — whatever a reader needs to
rebuild your setup.

## 4. Data

What you used, where it came from, and its licence. Flag anything personal or
non-redistributable, and keep it out of the repository (see `.gitignore`).
If data comes from human subjects or contains personal information, describe
how consent was obtained.

## 5. Evaluation

How you measured success: task, metric, baseline.

| Setup    | Metric | Result |
|----------|--------|--------|
| Baseline |        |        |
| Ours     |        |        |

## 6. Limitations

Where it breaks, what you did not test, and known failure modes.

## 7. Reproducibility

What a judge needs to get your numbers back: hardware, runtime, seeds, and the
exact commit. `make run` should do the rest.

## 8. Next steps

What you would build with another month.

## License

Creative Commons Attribution 4.0 (CC-BY-4.0). All HackApertus projects are open-sourced.

## References
