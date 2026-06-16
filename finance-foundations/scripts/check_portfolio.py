from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "PORTFOLIO.md",
    "CAREER_PORTFOLIO.md",
    "PROJECT_ONE_PAGERS.md",
    "SUBMISSION_CHECKLIST.md",
    "portfolio-assets/README.md",
    "portfolio-assets/contact-template.md",
    "portfolio-assets/writing-samples/investment-memo-template.md",
    "portfolio-assets/writing-samples/market-commentary-template.md",
    "portfolio-assets/presentation/pitch-deck-outline.md",
]

LEGACY_PROJECTS = [
    "capm-beta-calculator",
    "corporate-governance-analyzer",
    "market-efficiency-tester",
    "mispricing-risk-dashboard",
    "multifactor-model-lab",
    "option-pricing-engine",
    "portfolio-optimizer",
]

PRACTICAL_PROJECTS = {
    "01-financial-statement-analysis": {
        "command": ["src/analyze_financials.py"],
        "report": "financial_statement_analysis_report.md",
        "min_charts": 5,
    },
    "02-python-portfolio-analysis": {
        "command": ["src/main.py"],
        "report": "portfolio_analysis_report.md",
        "min_charts": 5,
    },
    "03-credit-risk-analysis": {
        "command": ["src/main.py"],
        "report": "credit_risk_analysis_report.md",
        "min_charts": 4,
    },
    "04-stock-valuation-dcf-comparables": {
        "command": ["src/main.py"],
        "report": "stock_valuation_report.md",
        "min_charts": 5,
    },
}


def run_python(script: str, cwd: Path) -> str:
    result = subprocess.run(
        [sys.executable, script],
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{cwd.name} failed with exit code {result.returncode}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result.stdout.strip()


def verify_legacy_projects() -> list[str]:
    results = []
    for project in LEGACY_PROJECTS:
        project_dir = ROOT / "projects" / project
        if not (project_dir / "README.md").exists():
            raise FileNotFoundError(f"Missing README: {project_dir}")
        output = run_python("main.py", project_dir)
        if not output:
            raise RuntimeError(f"{project} produced no output.")
        results.append(f"OK legacy: {project}")
    return results


def verify_required_docs() -> list[str]:
    results = []
    for rel_path in REQUIRED_DOCS:
        path = ROOT / rel_path
        if not path.exists() or path.stat().st_size == 0:
            raise FileNotFoundError(f"Missing required portfolio document: {path}")
        results.append(f"OK doc: {rel_path}")

    one_pagers = (ROOT / "PROJECT_ONE_PAGERS.md").read_text(encoding="utf-8")
    for heading in ["Problem", "Data / Source Used", "Method", "Key Assumptions", "Output / Recommendation", "What This Proves"]:
        if heading not in one_pagers:
            raise RuntimeError(f"PROJECT_ONE_PAGERS.md is missing section: {heading}")
    return results


def verify_practical_projects() -> list[str]:
    results = []
    practical_root = ROOT / "practical-projects"
    for project, spec in PRACTICAL_PROJECTS.items():
        project_dir = practical_root / project
        if not (project_dir / "README.md").exists():
            raise FileNotFoundError(f"Missing README: {project_dir}")
        run_python(spec["command"][0], project_dir)

        report = project_dir / "outputs" / "reports" / spec["report"]
        if not report.exists() or report.stat().st_size == 0:
            raise FileNotFoundError(f"Missing generated report: {report}")

        charts = list((project_dir / "outputs" / "charts").glob("*.png"))
        if len(charts) < spec["min_charts"]:
            raise RuntimeError(f"{project} expected at least {spec['min_charts']} charts, found {len(charts)}.")

        results.append(f"OK practical: {project} ({len(charts)} charts)")
    return results


def main() -> None:
    print("Checking finance portfolio projects...")
    results = verify_required_docs() + verify_legacy_projects() + verify_practical_projects()
    for line in results:
        print(line)
    print("Portfolio check passed.")


if __name__ == "__main__":
    main()
