from __future__ import annotations

import math
from typing import Iterable

import numpy as np
import pandas as pd


def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0 or pd.isna(denominator):
        return float("nan")
    return numerator / denominator


def calculate_return(start_price: float, end_price: float) -> float:
    return safe_divide(end_price - start_price, start_price)


def calculate_volatility(returns: Iterable[float], periods_per_year: int = 252) -> float:
    series = pd.Series(returns).dropna()
    if len(series) < 2:
        return float("nan")
    return float(series.std(ddof=1) * math.sqrt(periods_per_year))


def calculate_sharpe_ratio(returns: Iterable[float], risk_free_rate: float = 0.0, periods_per_year: int = 252) -> float:
    series = pd.Series(returns).dropna()
    if len(series) < 2:
        return float("nan")
    daily_rf = risk_free_rate / periods_per_year
    volatility = series.std(ddof=1)
    if volatility == 0 or pd.isna(volatility):
        return float("nan")
    return float(((series - daily_rf).mean() / volatility) * math.sqrt(periods_per_year))


def calculate_profit_margin(net_income: float, revenue: float) -> float:
    return safe_divide(net_income, revenue)


def calculate_roe(net_income: float, shareholders_equity: float) -> float:
    return safe_divide(net_income, shareholders_equity)


def calculate_current_ratio(current_assets: float, current_liabilities: float) -> float:
    return safe_divide(current_assets, current_liabilities)


def discount_cash_flow(cash_flows: Iterable[float], discount_rate: float) -> float:
    if discount_rate <= -1:
        raise ValueError("discount_rate must be greater than -100%.")
    return float(sum(cash_flow / ((1 + discount_rate) ** period) for period, cash_flow in enumerate(cash_flows, start=1)))


def annualized_return(returns: Iterable[float], periods_per_year: int = 252) -> float:
    series = pd.Series(returns).dropna()
    if series.empty:
        return float("nan")
    total_growth = float(np.prod(1 + series))
    years = len(series) / periods_per_year
    return total_growth ** (1 / years) - 1


def calculate_max_drawdown(cumulative_returns: pd.Series) -> float:
    wealth = 1 + cumulative_returns
    running_max = wealth.cummax()
    return float((wealth / running_max - 1).min())

