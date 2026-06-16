# Credit Risk Analysis Report

## Executive Summary

This project scores 20 fake borrowers. The average credit score is 586, average default probability is 52.6%, and 12 borrowers fall into high or very high risk categories.

## Data Used

Input file: `data/sample_credit_data.csv`

The dataset contains fake borrower income, debt-to-income, credit history, missed payments, existing debt, employment status, loan amount, and sample default flags.

## Key Metrics

- Borrowers scored: 20
- Average credit score: 586
- Average default probability: 52.6%
- High or very high risk borrowers: 12

## Dataset Overview

The dataset includes income, debt-to-income, credit history, missed payments, existing debt, employment status, loan amount, and a sample default flag.

## Credit Scoring Method

The score adjusts for income, credit history, employment, debt-to-income, missed payments, existing debt, and loan amount.

Chart: `../charts/credit_score_distribution.png`

## Default Probability Method

Default probability uses a logistic-shaped rule based on score plus risk-driver penalties.

Chart: `../charts/default_probability_distribution.png`

## Risk Segments

| risk_category | borrowers | avg_credit_score | avg_default_probability | avg_debt_to_income | default_rate |
| --- | --- | --- | --- | --- | --- |
| Low risk | 6 | 802 | 4.1% | 23.2% | 0.0% |
| Medium risk | 2 | 716 | 15.0% | 31.5% | 0.0% |
| High risk | 1 | 653 | 40.0% | 36.0% | 0.0% |
| Very high risk | 11 | 438 | 87.0% | 51.1% | 72.7% |

Chart: `../charts/risk_category_counts.png`

## Key Risk Drivers

- Missed payments.
- Debt-to-income above 40%.
- Unemployment.
- Large loan size relative to income.

Chart: `../charts/dti_vs_default_probability.png`

## Charts Generated

- `../charts/credit_score_distribution.png`
- `../charts/default_probability_distribution.png`
- `../charts/risk_category_counts.png`
- `../charts/dti_vs_default_probability.png`

## Article Insights

No project-specific articles have been processed yet. Add credit cycle or borrower-risk articles to `research/articles/` and use the shared article reader to turn risk drivers into model notes.

## Borrower Examples

### Safest Borrowers

| borrower_id | income | debt_to_income | credit_score | default_probability | risk_category |
| --- | --- | --- | --- | --- | --- |
| B018 | $135,000 | 19.0% | 835 | 2.0% | Low risk |
| B004 | $120,000 | 21.0% | 832 | 2.1% | Low risk |
| B001 | $95,000 | 18.0% | 823 | 2.4% | Low risk |

### Riskiest Borrowers

| borrower_id | income | debt_to_income | credit_score | default_probability | risk_category |
| --- | --- | --- | --- | --- | --- |
| B003 | $38,000 | 55.0% | 356 | 95.0% | Very high risk |
| B010 | $46,000 | 57.0% | 422 | 95.0% | Very high risk |
| B008 | $51,000 | 48.0% | 460 | 95.0% | Very high risk |

## Limitations

The model is fake, small, and not statistically validated. Real lending requires compliance, fairness, calibration, and monitoring.

## Final Conclusion

The rule-based model is useful for learning credit risk logic and screening borrowers, but it must be replaced or validated before any real lending use.
