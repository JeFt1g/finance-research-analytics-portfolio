from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from credit_charts import create_credit_charts
from credit_score_model import load_credit_data, score_borrowers
from default_probability import add_default_probability
from risk_segments import add_risk_segments, segment_summary
from utils.report_helpers import format_currency, format_number, format_percent, markdown_table


def build_report(df: pd.DataFrame, segments: pd.DataFrame, charts: dict[str, Path]) -> str:
    high_risk = df[df["risk_category"].isin(["High risk", "Very high risk"])]
    safest = df.sort_values("default_probability").head(3)[["borrower_id", "income", "debt_to_income", "credit_score", "default_probability", "risk_category"]]
    riskiest = df.sort_values("default_probability", ascending=False).head(3)[["borrower_id", "income", "debt_to_income", "credit_score", "default_probability", "risk_category"]]
    borrower_formatters = {
        "income": lambda value: format_currency(value, digits=0, suffix=""),
        "debt_to_income": format_percent,
        "credit_score": lambda value: format_number(value, 0),
        "default_probability": format_percent,
    }
    segment_formatters = {
        "avg_credit_score": lambda value: format_number(value, 0),
        "avg_default_probability": format_percent,
        "avg_debt_to_income": format_percent,
        "default_rate": format_percent,
    }
    risk_view = f"{len(high_risk)} borrowers fall into high or very high risk categories."
    return f"""# Credit Risk Analysis Report

## Executive Summary

This project scores {len(df)} fake borrowers. The average credit score is {format_number(df['credit_score'].mean(), 0)}, average default probability is {format_percent(df['default_probability'].mean())}, and {risk_view}

## Data Used

Input file: `data/sample_credit_data.csv`

The dataset contains fake borrower income, debt-to-income, credit history, missed payments, existing debt, employment status, loan amount, and sample default flags.

## Key Metrics

- Borrowers scored: {len(df)}
- Average credit score: {format_number(df['credit_score'].mean(), 0)}
- Average default probability: {format_percent(df['default_probability'].mean())}
- High or very high risk borrowers: {len(high_risk)}

## Dataset Overview

The dataset includes income, debt-to-income, credit history, missed payments, existing debt, employment status, loan amount, and a sample default flag.

## Credit Scoring Method

The score adjusts for income, credit history, employment, debt-to-income, missed payments, existing debt, and loan amount.

Chart: `../charts/{charts['credit_score_distribution'].name}`

## Default Probability Method

Default probability uses a logistic-shaped rule based on score plus risk-driver penalties.

Chart: `../charts/{charts['default_probability_distribution'].name}`

## Risk Segments

{markdown_table(segments, segment_formatters)}

Chart: `../charts/{charts['risk_category_counts'].name}`

## Key Risk Drivers

- Missed payments.
- Debt-to-income above 40%.
- Unemployment.
- Large loan size relative to income.

Chart: `../charts/{charts['dti_vs_default_probability'].name}`

## Charts Generated

- `../charts/{charts['credit_score_distribution'].name}`
- `../charts/{charts['default_probability_distribution'].name}`
- `../charts/{charts['risk_category_counts'].name}`
- `../charts/{charts['dti_vs_default_probability'].name}`

## Article Insights

No project-specific articles have been processed yet. Add credit cycle or borrower-risk articles to `research/articles/` and use the shared article reader to turn risk drivers into model notes.

## Borrower Examples

### Safest Borrowers

{markdown_table(safest, borrower_formatters)}

### Riskiest Borrowers

{markdown_table(riskiest, borrower_formatters)}

## Limitations

The model is fake, small, and not statistically validated. Real lending requires compliance, fairness, calibration, and monitoring.

## Final Conclusion

The rule-based model is useful for learning credit risk logic and screening borrowers, but it must be replaced or validated before any real lending use.
"""


def main() -> None:
    data = load_credit_data()
    scored = score_borrowers(data)
    probabilities = add_default_probability(scored)
    segmented = add_risk_segments(probabilities)
    segments = segment_summary(segmented)
    charts = create_credit_charts(segmented, PROJECT_DIR / "outputs" / "charts")
    report = build_report(segmented, segments, charts)
    report_path = PROJECT_DIR / "outputs" / "reports" / "credit_risk_analysis_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    print(f"Wrote report: {report_path}")
    for chart in charts.values():
        print(f"Wrote chart: {chart}")


if __name__ == "__main__":
    main()
