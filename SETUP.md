# OpenParlData Extract — repo setup

## Location

`C:\Users\mdhat\Desktop\openparldata-extract`  
GitHub: _created on push — see below_

## Two Hack Apertus apps

| Project | Track | Folder | Desktop path |
| --- | --- | --- | --- |
| GemeindeSim | 2B Own Project | `gemeindesim/track_2b/` | `Desktop\gemeindesim` |
| **OpenParlData Extract** | **2A OpenParlData** | **`track_2a/`** | **`Desktop\openparldata-extract`** |

Each repo is a separate submission with its own `make run`, technical report, and demo video.

## Fork / push

```powershell
cd C:\Users\mdhat\Desktop\openparldata-extract
git remote rename origin template-upstream   # if not already done
git add -A
git commit -m "Initialize OpenParlData Track 2A submission"
git remote add origin https://github.com/YOUR_USER/openparldata-extract.git
git push -u origin main
```

Set the repo **public** before the 16 Oct deadline.

## Config

```powershell
cd track_2a
copy .env.example .env
```

Never commit `.env` or full copyrighted PDFs without licence notes in `technical_report.md`.
