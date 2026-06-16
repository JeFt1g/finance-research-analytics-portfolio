from __future__ import annotations

import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "src"))

from portfolio_returns import calculate_daily_returns, calculate_portfolio_returns, load_prices, load_weights
from risk_metrics import portfolio_risk_summary


def test_sample_data_loads() -> None:
    prices = load_prices()
    weights = load_weights()
    assert not prices.empty
    assert abs(weights.sum() - 1.0) < 0.0001


def test_main_calculations_work() -> None:
    returns = calculate_daily_returns(load_prices())
    portfolio_returns = calculate_portfolio_returns(returns, load_weights())
    summary = portfolio_risk_summary(portfolio_returns)
    assert "sharpe_ratio" in summary


def test_output_folders_exist() -> None:
    assert (PROJECT_DIR / "outputs" / "reports").exists()
    assert (PROJECT_DIR / "outputs" / "charts").exists()


if __name__ == "__main__":
    test_sample_data_loads()
    test_main_calculations_work()
    test_output_folders_exist()
