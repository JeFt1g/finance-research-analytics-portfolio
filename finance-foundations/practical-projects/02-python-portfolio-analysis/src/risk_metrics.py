from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.finance_math import annualized_return, calculate_max_drawdown, calculate_sharpe_ratio, calculate_volatility


def portfolio_risk_summary(portfolio_returns: pd.Series, risk_free_rate: float = 0.02) -> dict[str, float]:
    cumulative = (1 + portfolio_returns).cumprod() - 1
    return {
        "total_return": float(cumulative.iloc[-1]),
        "annualized_return": annualized_return(portfolio_returns),
        "annualized_volatility": calculate_volatility(portfolio_returns),
        "sharpe_ratio": calculate_sharpe_ratio(portfolio_returns, risk_free_rate),
        "max_drawdown": calculate_max_drawdown(cumulative),
    }


def asset_risk_return(asset_returns: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "ticker": ticker,
                "annualized_return": annualized_return(asset_returns[ticker]),
                "annualized_volatility": calculate_volatility(asset_returns[ticker]),
            }
            for ticker in asset_returns.columns
        ]
    )


def correlation_matrix(asset_returns: pd.DataFrame) -> pd.DataFrame:
    return asset_returns.corr()

