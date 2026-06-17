from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "README.md",
    "PORTFOLIO.md",
    "HOW_TO_RUN.md",
    "PROJECT_INDEX.md",
    "RESEARCH_INDEX.md",
    "ARTICLE_LIBRARY.md",
]

REQUIRED_APPS = [
    "apps/finance_research_app/app.py",
    "apps/project_dashboard_launcher/app.py",
]

PRACTICAL_PROJECTS = {
    "01-financial-statement-analysis": {
        "command": "main.py",
        "report": "financial_statement_analysis_report.md",
        "min_charts": 5,
        "min_screenshots": 3,
    },
    "02-python-portfolio-analysis": {
        "command": "main.py",
        "report": "portfolio_analysis_report.md",
        "min_charts": 5,
        "min_screenshots": 3,
    },
    "03-credit-risk-analysis": {
        "command": "main.py",
        "report": "credit_risk_analysis_report.md",
        "min_charts": 4,
        "min_screenshots": 3,
    },
    "04-stock-valuation-dcf-comparables": {
        "command": "main.py",
        "report": "stock_valuation_report.md",
        "min_charts": 5,
        "min_screenshots": 3,
    },
}


def run_python(script: str, cwd: Path, args: list[str] | None = None) -> str:
    command = [sys.executable, script, *(args or [])]
    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{cwd.name} failed with exit code {result.returncode}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result.stdout.strip()


def verify_required_docs() -> list[str]:
    results = []
    for rel_path in REQUIRED_DOCS:
        path = ROOT / rel_path
        if not path.exists() or path.stat().st_size == 0:
            raise FileNotFoundError(f"Missing required portfolio document: {path}")
        results.append(f"OK doc: {rel_path}")
    return results


def verify_apps() -> list[str]:
    results = []
    for rel_path in REQUIRED_APPS:
        path = ROOT / rel_path
        if not path.exists() or path.stat().st_size == 0:
            raise FileNotFoundError(f"Missing app file: {path}")
        results.append(f"OK app: {rel_path}")
    return results


def verify_article_reader() -> list[str]:
    reader = ROOT / "shared" / "article_reader" / "article_reader.py"
    sample = ROOT / "research" / "articles" / "sample_company_article.txt"
    processed = ROOT / "research" / "processed"
    if not reader.exists():
        raise FileNotFoundError(f"Missing article reader: {reader}")
    if not sample.exists():
        raise FileNotFoundError(f"Missing sample article: {sample}")
    run_python(str(reader), ROOT, ["--input", str(sample.relative_to(ROOT))])
    outputs = list(processed.glob("*_analysis.md"))
    if not outputs:
        raise RuntimeError("Article reader did not produce processed markdown outputs.")
    return [f"OK article reader: {len(outputs)} processed files"]


def verify_practical_projects() -> list[str]:
    results = []
    practical_root = ROOT / "practical-projects"
    for project, spec in PRACTICAL_PROJECTS.items():
        project_dir = practical_root / project
        if not (project_dir / "README.md").exists():
            raise FileNotFoundError(f"Missing README: {project_dir}")
        run_python(spec["command"], project_dir)

        report = project_dir / "outputs" / "reports" / spec["report"]
        if not report.exists() or report.stat().st_size == 0:
            raise FileNotFoundError(f"Missing generated report: {report}")

        charts = list((project_dir / "outputs" / "charts").glob("*.png"))
        if len(charts) < spec["min_charts"]:
            raise RuntimeError(f"{project} expected at least {spec['min_charts']} charts, found {len(charts)}.")

        screenshots = list((project_dir / "outputs" / "screenshots").glob("*.png"))
        if len(screenshots) < spec["min_screenshots"]:
            raise RuntimeError(
                f"{project} expected at least {spec['min_screenshots']} screenshots, found {len(screenshots)}."
            )

        results.append(f"OK practical: {project} ({len(charts)} charts, {len(screenshots)} screenshots)")
    return results


def main() -> None:
    print("Checking finance portfolio...")
    results = verify_required_docs() + verify_apps() + verify_article_reader() + verify_practical_projects()
    for line in results:
        print(line)
    print("Portfolio check passed.")


if __name__ == "__main__":
    main()
