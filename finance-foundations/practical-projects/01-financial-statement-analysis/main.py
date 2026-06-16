from __future__ import annotations

import runpy
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
SRC_DIR = PROJECT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))


def main() -> None:
    runpy.run_path(str(SRC_DIR / "analyze_financials.py"), run_name="__main__")


if __name__ == "__main__":
    main()
