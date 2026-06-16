# Financial Statement Analysis Report

## Company Analyzed

Apple-style fake sample company from 2020 through 2025.

## Executive Summary

The company generated $412,210.0M of revenue and $110,940.0M of net income in 2025. Latest revenue growth was 5.4%, net margin was 26.9%, and ROE was 158.0%.

## Data Used

Input file: `data/apple_sample_financials.csv`

The dataset contains fake annual financial statement data for revenue, gross profit, operating income, net income, current assets, current liabilities, total assets, shareholders' equity, and total debt.

## Key Metrics

- Latest revenue growth: 5.4%
- Gross margin: 46.9%
- Operating margin: 32.4%
- Net margin: 26.9%
- ROE: 158.0%
- Current ratio: 1.05
- Debt-to-equity: 1.44

## Revenue Trend

Revenue growth is healthy in the latest year.

Chart: `../charts/revenue_trend.png`

## Profitability Trend

Net margin improved.

Chart: `../charts/net_income_trend.png`

## Ratio Analysis

| year | gross_margin | operating_margin | net_profit_margin | roe | current_ratio | debt_to_equity | asset_turnover |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022.0 | 43.3% | 30.3% | 25.3% | 197.0% | 0.88 | 2.37 | 1.12 |
| 2023.0 | 44.1% | 29.8% | 25.3% | 156.1% | 0.99 | 1.79 | 1.09 |
| 2024.0 | 46.2% | 31.5% | 26.2% | 157.8% | 1.01 | 1.64 | 1.07 |
| 2025.0 | 46.9% | 32.4% | 26.9% | 158.0% | 1.05 | 1.44 | 1.09 |

Chart: `../charts/margin_comparison.png`

## Key Insights

- Revenue reached the highest level in the sample period.
- Operating income and net income grew in the latest year.
- ROE remains high.
- Current ratio is close to 1.0, so liquidity is adequate but not excessive.
- Debt-to-equity declined, reducing balance sheet risk.

## Charts Generated

- `../charts/revenue_trend.png`
- `../charts/net_income_trend.png`
- `../charts/margin_comparison.png`
- `../charts/roe_trend.png`
- `../charts/liquidity_trend.png`

## Article Insights

No project-specific articles have been processed yet. Add company articles to `research/articles/` and use the shared article reader to link margin, governance, and valuation risks into this report.

## Key Risks

- Annual data hides quarterly volatility.
- High ROE can be flattered by leverage or buybacks.
- Liquidity needs cash flow timing, not just current ratio.

## Limitations

The dataset is fake, annual, and simplified. Real analysis should use filings, segment data, cash flow details, footnotes, and peer benchmarks.

## Final Conclusion

The sample company appears financially strong, with renewed growth, improving margins, and lower leverage. The main watch item is liquidity close to 1.0.
