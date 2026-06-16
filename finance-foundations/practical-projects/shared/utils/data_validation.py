from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_csv(path: Path | str) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")
    return pd.read_csv(path)


def require_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def require_no_missing(df: pd.DataFrame, columns: Iterable[str] | None = None) -> None:
    target_columns = list(columns) if columns is not None else list(df.columns)
    missing = df[target_columns].isna().sum()
    offenders = missing[missing > 0]
    if not offenders.empty:
        details = ", ".join(f"{name}={count}" for name, count in offenders.items())
        raise ValueError(f"Missing values found: {details}")


def require_numeric_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    non_numeric = [column for column in columns if not pd.api.types.is_numeric_dtype(df[column])]
    if non_numeric:
        raise TypeError(f"Columns must be numeric: {', '.join(non_numeric)}")

