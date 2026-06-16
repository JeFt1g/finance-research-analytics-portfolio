from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def require_file(path: Path | str) -> Path:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    if not path.is_file():
        raise ValueError(f"Expected a file path, got: {path}")
    return path


def require_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def require_numeric_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    non_numeric = [column for column in columns if not pd.api.types.is_numeric_dtype(df[column])]
    if non_numeric:
        raise TypeError(f"Columns must be numeric: {', '.join(non_numeric)}")


def require_no_missing(df: pd.DataFrame, columns: Iterable[str] | None = None) -> None:
    target_columns = list(columns) if columns is not None else list(df.columns)
    missing = df[target_columns].isna().sum()
    offenders = missing[missing > 0]
    if not offenders.empty:
        details = ", ".join(f"{column}={count}" for column, count in offenders.items())
        raise ValueError(f"Missing values found: {details}")


def load_csv_checked(path: Path | str, required_columns: Iterable[str] | None = None, numeric_columns: Iterable[str] | None = None) -> pd.DataFrame:
    file_path = require_file(path)
    df = pd.read_csv(file_path)
    if required_columns is not None:
        require_columns(df, required_columns)
    if numeric_columns is not None:
        require_numeric_columns(df, numeric_columns)
    require_no_missing(df, required_columns)
    return df
