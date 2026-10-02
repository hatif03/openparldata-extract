"""Entry point: `python -m opd_extract`."""

from __future__ import annotations

import os
import sys


def main() -> None:
    name = os.environ.get("LLM_NAME", "apertus-v1.5-70b")
    base = os.environ.get("LLM_BASE_URL", "https://hackapertus.livemap.sh/v1")
    key = os.environ.get("LLM_API_KEY", "")

    print("OpenParlData Extract (stub)")
    print(f"  LLM_NAME={name}")
    print(f"  LLM_BASE_URL={base}")
    if not key:
        print("  LLM_API_KEY is not set — copy .env.example to .env", file=sys.stderr)
        sys.exit(1)
    print("  LLM_API_KEY=***")
    print()
    print("Pipeline not implemented yet. See docs/CHALLENGE.md and docs/ARCHITECTURE.md.")
    sys.exit(0)


if __name__ == "__main__":
    main()
