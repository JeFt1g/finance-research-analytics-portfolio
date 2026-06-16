from __future__ import annotations

import math
from typing import Iterable

import numpy as np
import pandas as pd


TRADING_DAYS = 252


def returns(prices: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    return prices.pct_change().dropna()


def cumulative_returns(period_returns: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    return (1 + period_returns).cumprod() - 1


def annualized_return(period_returns: pd.Series, periods_per_year: int = TRADING_DAYS) -> float:
    if period_returns.empty:
        return 0.0
    growth = float((1 + period_returns).prod())
    years = len(period_returns) / periods_per_year
    if years <= 0 or growth <= 0:
        return 0.0
    return growth ** (1 / years) - 1


def volatility(period_returns: pd.Series, periods_per_year: int = TRADING_DAYS) -> float:
    return float(period_returns.std(ddof=1) * math.sqrt(periods_per_year))


def sharpe_ratio(period_returns: pd.Series, risk_free_rate: float = 0.0, periods_per_year: int = TRADING_DAYS) -> float:
    annual_return = annualized_return(period_returns, periods_per_year)
    annual_vol = volatility(period_returns, periods_per_year)
    if annual_vol == 0:
        return 0.0
    return float((annual_return - risk_free_rate) / annual_vol)


def max_drawdown(values: pd.Series) -> float:
    if values.empty:
        return 0.0
    running_max = values.cummax()
    drawdown = values / running_max - 1
    return float(drawdown.min())


def profit_margin(profit: float, revenue: float) -> float:
    return 0.0 if revenue == 0 else float(profit / revenue)


def roe(net_income: float, shareholders_equity: float) -> float:
    return 0.0 if shareholders_equity == 0 else float(net_income / shareholders_equity)


def current_ratio(current_assets: float, current_liabilities: float) -> float:
    return 0.0 if current_liabilities == 0 else float(current_assets / current_liabilities)


def debt_to_equity(total_debt: float, shareholders_equity: float) -> float:
    return 0.0 if shareholders_equity == 0 else float(total_debt / shareholders_equity)


def dcf_present_value(cash_flows: Iterable[float], discount_rate: float) -> float:
    if discount_rate <= -1:
        raise ValueError("Discount rate must be greater than -100%.")
    return float(sum(cash_flow / ((1 + discount_rate) ** index) for index, cash_flow in enumerate(cash_flows, start=1)))


def cagr(start_value: float, end_value: float, years: float) -> float:
    if start_value <= 0 or years <= 0:
        return 0.0
    return float((end_value / start_value) ** (1 / years) - 1)


def weighted_average(values: Iterable[float], weights: Iterable[float]) -> float:
    values_array = np.array(list(values), dtype=float)
    weights_array = np.array(list(weights), dtype=float)
    if weights_array.sum() == 0:
        raise ValueError("Weights must not sum to zero.")
    return float(np.average(values_array, weights=weights_array))
