from __future__ import annotations

from typing import Callable

import pandas as pd


def format_percent(value: float, digits: int = 1) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{value * 100:.{digits}f}%"


def format_number(value: float, digits: int = 1) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{value:,.{digits}f}"


def format_currency(value: float, digits: int = 1, suffix: str = "M") -> str:
    if pd.isna(value):
        return "n/a"
    return f"${value:,.{digits}f}{suffix}"


def markdown_table(df: pd.DataFrame, formatters: dict[str, Callable[[float], str]] | None = None) -> str:
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

