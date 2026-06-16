from __future__ import annotations

import argparse
import re
from pathlib import Path

from article_summarizer import clean_text, summarize_text
from connect_article_to_project import project_connections
from connect_article_to_theory import theory_connections
from extract_financial_insights import (
    FINANCE_KEYWORDS,
    RISK_WORDS,
    extract_companies,
    extract_key_financial_points,
    extract_matching_terms,
    extract_numbers,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
SUPPORTED_EXTENSIONS = {".txt", ".md", ".pdf"}


def read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except Exception as exc:
        raise RuntimeError("PDF reading requires pypdf. Install requirements.txt or use .txt/.md input.") from exc
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def read_article(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md"}:
        return path.read_text(encoding="utf-8")
    if suffix == ".pdf":
        return read_pdf(path)
    raise ValueError(f"Unsupported article file type: {path.suffix}")


def iter_input_files(input_path: Path) -> list[Path]:
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() in SUPPORTED_EXTENSIONS else []
    if not input_path.exists():
        raise FileNotFoundError(f"Missing input path: {input_path}")
    return sorted(path for path in input_path.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS)


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None detected."


def possible_app_ideas(theories: list[str], projects: list[str]) -> list[str]:
    ideas = []
    joined = " ".join(theories + projects).lower()
    if "stock valuation" in joined:
        ideas.append("Add the article as a risk or assumptions note in the Stock Valuation app.")
    if "portfolio" in joined:
        ideas.append("Use the article to define a portfolio stress scenario or allocation note.")
    if "credit" in joined:
        ideas.append("Convert the article's risk drivers into credit score model features.")
    if "market efficiency" in joined:
        ideas.append("Turn the event into an abnormal-return study.")
    if "black-scholes" in joined:
        ideas.append("Use the article to motivate an option volatility dashboard.")
    return ideas or ["Create a short source note and link it to the most relevant theory folder."]


def analyze_text(text: str, source: Path | str = "pasted text") -> dict[str, object]:
    cleaned = clean_text(text)
    theory_matches = theory_connections(cleaned)
    project_matches = project_connections(cleaned)
    return {
        "source": str(source),
        "word_count": len(re.findall(r"\b\w+\b", cleaned)),
        "summary": summarize_text(cleaned),
        "financial_points": extract_key_financial_points(cleaned),
        "numbers": extract_numbers(cleaned),
        "companies": extract_companies(cleaned),
        "risks": extract_matching_terms(cleaned, RISK_WORDS),
        "finance_keywords": extract_matching_terms(cleaned, FINANCE_KEYWORDS),
        "theory_connections": theory_matches,
        "project_connections": project_matches,
        "app_ideas": possible_app_ideas(theory_matches, project_matches),
        "questions": [
            "What source data would confirm the article's main claim?",
            "Which assumptions are most sensitive to being wrong?",
            "Can this article become a chart, ratio, scenario, or case study?",
        ],
    }


def render_markdown(analysis: dict[str, object]) -> str:
    return f"""# Article Analysis

## Source File

{analysis['source']}

## Short Summary

{bullet_list(analysis['summary'])}

## Key Financial Points

{bullet_list(analysis['financial_points'])}

## Important Numbers

{bullet_list(analysis['numbers'])}

## Companies Mentioned

{bullet_list(analysis['companies'])}

## Risks Mentioned

{bullet_list(analysis['risks'])}

## Finance Keywords

{bullet_list(analysis['finance_keywords'])}

## Theory Connections

{bullet_list(analysis['theory_connections'])}

## Project Connections

{bullet_list(analysis['project_connections'])}

## Possible App Ideas

{bullet_list(analysis['app_ideas'])}

## Questions To Research Next

{bullet_list(analysis['questions'])}

## Reader Limitations

This reader uses local rule-based extraction. It is useful for organizing research, but it does not replace professional financial analysis or full language-model reasoning.
"""


def process_file(path: Path, output_dir: Path) -> Path:
    text = read_article(path)
    analysis = analyze_text(text, path)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{path.stem}_analysis.md"
    output_path.write_text(render_markdown(analysis), encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rule-based local article reader for finance research.")
    parser.add_argument("--input", required=True, help="Article file or folder under research/articles.")
    parser.add_argument("--output", default=str(REPO_ROOT / "research" / "processed"), help="Folder for processed markdown outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output)
    files = iter_input_files(input_path)
    if not files:
        raise SystemExit(f"No supported article files found in {input_path}")
    for file_path in files:
        output_path = process_file(file_path, output_dir)
        print(f"Wrote analysis: {output_path}")


if __name__ == "__main__":
    main()
