from __future__ import annotations

import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "src"))

from credit_score_model import load_credit_data, score_borrowers
from default_probability import add_default_probability
from risk_segments import add_risk_segments, segment_summary


def test_sample_data_loads() -> None:
    df = load_credit_data()
    assert not df.empty
    assert "borrower_id" in df.columns


def test_main_calculations_work() -> None:
    scored = score_borrowers(load_credit_data())
    probabilities = add_default_probability(scored)
    segmented = add_risk_segments(probabilities)
    summary = segment_summary(segmented)
    assert "risk_category" in segmented.columns
    assert not summary.empty


def test_output_folders_exist() -> None:
    assert (PROJECT_DIR / "outputs" / "reports").exists()
    assert (PROJECT_DIR / "outputs" / "charts").exists()


if __name__ == "__main__":
    test_sample_data_loads()
    test_main_calculations_work()
    test_output_folders_exist()
