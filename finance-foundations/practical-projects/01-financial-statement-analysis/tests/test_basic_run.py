from __future__ import annotations

import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "src"))

from ratio_analysis import calculate_ratios, load_financials
from trend_analysis import calculate_trends


def test_sample_data_loads() -> None:
    df = load_financials()
    assert not df.empty
    assert "revenue" in df.columns


def test_main_calculations_work() -> None:
    ratios = calculate_ratios(load_financials())
    trends = calculate_trends(ratios)
    assert "net_profit_margin" in ratios.columns
    assert "revenue_growth" in trends.columns


def test_output_folders_exist() -> None:
    assert (PROJECT_DIR / "outputs" / "reports").exists()
    assert (PROJECT_DIR / "outputs" / "charts").exists()


if __name__ == "__main__":
    test_sample_data_loads()
    test_main_calculations_work()
    test_output_folders_exist()
