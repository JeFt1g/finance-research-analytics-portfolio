from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.data_validation import load_csv, require_columns, require_no_missing, require_numeric_columns


def load_prices(path: Path | None = None) -> pd.DataFrame:
    prices = load_csv(path or PROJECT_DIR / "data" / "sample_portfolio_prices.csv")
    require_columns(prices, ["date"])
    require_no_missing(prices)
    prices["date"] = pd.to_datetime(prices["date"])
    numeric_columns = [column for column in prices.columns if column != "date"]
    require_numeric_columns(prices, numeric_columns)
    return prices.sort_values("date").set_index("date")


def load_weights(path: Path | None = None) -> pd.Series:
    weights = load_csv(path or PROJECT_DIR / "data" / "sample_portfolio_weights.csv")
    require_columns(weights, ["ticker", "weight"])
    require_no_missing(weights, ["ticker", "weight"])
    require_numeric_columns(weights, ["weight"])
    series = weights.set_index("ticker")["weight"].astype(float)
    return series / series.sum()


def calculate_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return prices.pct_change().dropna()


def calculate_portfolio_returns(asset_returns: pd.DataFrame, weights: pd.Series) -> pd.Series:
    missing = [ticker for ticker in weights.index if ticker not in asset_returns.columns]
    if missing:
        raise ValueError(f"Missing price history for weighted tickers: {', '.join(missing)}")
    return asset_returns.dot(weights.reindex(asset_returns.columns).fillna(0)).rename("portfolio_return")


def calculate_cumulative_returns(returns: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    return (1 + returns).cumprod() - 1


def calculate_portfolio_value(portfolio_returns: pd.Series, initial_value: float = 10000.0) -> pd.Series:
    return (initial_value * (1 + portfolio_returns).cumprod()).rename("portfolio_value")

