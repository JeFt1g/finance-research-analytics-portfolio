from __future__ import annotations

import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "src"))

from comparables_analysis import calculate_multiples, load_comparables
from dcf_model import build_dcf, get_assumption, load_assumptions, load_financials
from sensitivity_analysis import build_sensitivity_table


def test_sample_data_loads() -> None:
    financials = load_financials()
    assumptions = load_assumptions()
    comparables = load_comparables()
    assert not financials.empty
    assert not assumptions.empty
    assert not comparables.empty


def test_main_calculations_work() -> None:
    financials = load_financials()
    assumption = get_assumption(load_assumptions(), "Base")
    forecast, summary = build_dcf(financials, assumption)
    sensitivity = build_sensitivity_table(financials, assumption)
    multiples = calculate_multiples(load_comparables())
    assert not forecast.empty
    assert summary["implied_share_price"] > 0
    assert not sensitivity.empty
    assert "ev_revenue" in multiples.columns


def test_output_folders_exist() -> None:
    assert (PROJECT_DIR / "outputs" / "reports").exists()
    assert (PROJECT_DIR / "outputs" / "charts").exists()


if __name__ == "__main__":
    test_sample_data_loads()
    test_main_calculations_work()
    test_output_folders_exist()
