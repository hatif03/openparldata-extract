# OpenParlData Extract

**Track 2A — OpenParlData / BFH:** turn messy Swiss parliamentary affair PDFs into **one structured representation** aligned with [OpenParlData](https://openparldata.ch/home) and **eCH-0295**, using layout tools (Docling/Marker) plus **Apertus 1.5** for schema mapping.

- **Hackathon:** [Hack Apertus](https://hackapertus.ch/) online stage, 1–16 October 2026  
- **Track:** [Track 2A — Academia](track_2a/README.md) · challenge **OpenParlData**  
- **Sibling project:** [GemeindeSim](https://github.com/hatif03/gemeindesim) (Track 2B — own civic simulation)  
- **Study notes:** `C:\Users\mdhat\Desktop\apertus\track-2a\openparldata\` on this machine  

## Layout

| Path | Purpose |
| --- | --- |
| `track_2a/` | **Submission root** (do not rename) |
| `track_2a/src/` | Extraction pipeline code |
| `track_2a/data/` | Sample PDFs / gold snippets (max. 100 MB) |
| `track_2a/docs/` | Challenge brief, hackathon links, architecture |

## Quick start

```bash
cp track_2a/.env.example track_2a/.env   # set LLM_API_KEY
make run
```

See [SETUP.md](SETUP.md) and [track_2a/docs/HACKATHON.md](track_2a/docs/HACKATHON.md).
