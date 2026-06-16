from __future__ import annotations

from pathlib import Path
from typing import Callable

import pandas as pd


def markdown_table(df: pd.DataFrame, formatters: dict[str, Callable[[object], str]] | None = None) -> str:
    formatters = formatters or {}
    columns = list(df.columns)
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    rows = []
    for _, row in df.iterrows():
        values = []
        for column in columns:
            value = row[column]
            values.append(formatters[column](value) if column in formatters else str(value))
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join([header, separator, *rows])


def executive_summary(title: str, bullets: list[str]) -> str:
    body = "\n".join(f"- {bullet}" for bullet in bullets)
    return f"## {title}\n\n{body}\n"


def chart_references(charts: dict[str, Path]) -> str:
    lines = ["## Charts Generated", ""]
    for name, path in charts.items():
        lines.append(f"- {name}: `{path}`")
    return "\n".join(lines)


def save_markdown_report(path: Path | str, title: str, sections: list[str]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n\n".join([f"# {title}", *sections]).rstrip() + "\n"
    path.write_text(content, encoding="utf-8")
    return path
