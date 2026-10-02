# Hack Apertus — context for OpenParlData Extract

## This submission

| Field | Value |
| --- | --- |
| Track | **2A — Academia Challenges** |
| Challenge | **OpenParlData** — PDFs → one structure |
| Partner | BFH / OpenParlData / eCH Political Affairs |
| Repo layout | `track_2a/` (unchanged name) |

Second application on the same hackathon: [GemeindeSim](https://github.com/hatif03/gemeindesim) (Track 2B).

## Official links

| Resource | URL |
| --- | --- |
| Programme | https://hackapertus.ch/ |
| Devpost | https://hackapertus.devpost.com/ |
| Getting started (Notion) | https://hackapertus.notion.site/getting-started-guide-onlinehack |
| Resources & tools | https://hackapertus.notion.site/resources-tools |
| Notion hub | https://hackapertus.notion.site/ |
| Template | https://github.com/HackApertus/project-template |
| **Submissions** | http://hackapertus.ch/online-hack/submissions |
| Discord | https://discord.gg/hack-apertus |
| Contact | hello@hackapertus.ch |

## Timeline (CEST)

| When | What |
| --- | --- |
| 1 Oct 2026, 12:00 | Hacking starts; challenge specs in Notion |
| 2 Oct 2026 | Partner deep dives (OpenParlData Luma — Discord) |
| **16 Oct 2026, 12:00** | **Deadline** (no extension) |
| 23 Oct 2026, 12:00 | Estimated winners |

## Track 2A — all five challenges

- FHGR — interview coach  
- **OpenParlData — parliamentary PDFs (this repo)**  
- OST — voting booklets NLI  
- UZH — cross-lingual government sites  
- ZHAW — robot arm VLM  

Judging criteria are **per challenge** in the getting-started guide (not the Track 2B five-dimension rubric).

## Submission checklist (2A)

- [ ] Public Git repo from template; only `track_2a/` kept  
- [ ] `make run` works via Docker from repo root  
- [ ] `technical_report.md` + PDF upload per organizer instructions  
- [ ] Demo video (if required for your challenge — confirm in Notion)  
- [ ] `data/` ≤ 100 MB; licensing documented  
- [ ] Submit at hackapertus.ch (not Devpost alone)  

## Apertus inference (hackathon)

```text
LLM_NAME=apertus-v1.5-70b
LLM_BASE_URL=https://hackapertus.livemap.sh/v1
LLM_API_KEY=<your key>
```

Model ids on the gateway differ from Hugging Face names (`swiss-ai/Apertus-v1.5-70B`).

Docs: https://www.apertus-ai.org/pages/documentation/  
API/tools: https://blog.nlp-lab.ai/2026/10/01/Apertus15GettingStarted.html

## Apertus usage notes (shared with GemeindeSim)

- Prefer **70B** for schema mapping quality; **8B** for bulk retry/fallback.  
- **JSON mode** + concrete example object + Pydantic gate.  
- **No parallel tool calls** in one completion; batch retrieval in code.  
- **Thinking** and **tools** not in the same request.  
- Multimodal: use page images only when Docling fails — keep eval honest.
