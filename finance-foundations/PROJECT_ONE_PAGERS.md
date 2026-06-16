# Project One-Pagers

Use these summaries for a career portfolio, networking email, interview prep, or project archive. Each project follows the same format: problem, data/source, method, assumptions, output, and what it proves.

## 1. Stock Valuation: DCF + Comparables

Project folder: [04-stock-valuation-dcf-comparables](practical-projects/04-stock-valuation-dcf-comparables/README.md)

### Problem

Estimate whether a Tesla-style company appears undervalued, fairly valued, or overvalued based on projected cash flows and peer valuation multiples.

### Data / Source Used

Fake educational company financials, DCF assumptions, and comparable company data stored in CSV files under the project `data/` folder.

### Method

Built a base-case DCF model, bull/base/bear scenarios, peer multiple comparison, and sensitivity analysis across discount rates and terminal growth rates.

### Key Assumptions

- Revenue growth, operating margin, tax rate, reinvestment rate, discount rate, and terminal growth drive the DCF.
- Net debt and shares outstanding convert enterprise value into implied share price.
- Comparable valuation uses median peer EV/Revenue, EV/EBITDA, and P/E.

### Output / Recommendation

The generated report provides implied share price, valuation range, peer-implied values, sensitivity results, and a final overvalued/fairly valued/undervalued conclusion for the fake dataset.

Report: `practical-projects/04-stock-valuation-dcf-comparables/outputs/reports/stock_valuation_report.md`

### What This Proves

DCF modeling, peer valuation, sensitivity analysis, investment recommendation framing, and clear valuation risk communication.

## 2. Financial Statement Analysis

Project folder: [01-financial-statement-analysis](practical-projects/01-financial-statement-analysis/README.md)

### Problem

Analyze whether a company is growing, profitable, liquid, efficient, and financially healthy using annual financial statements.

### Data / Source Used

Fake Apple-style annual income statement and balance sheet data stored in `apple_sample_financials.csv`.

### Method

Calculated year-over-year growth, margin ratios, ROE, current ratio, debt-to-equity, and asset turnover. Generated trend charts and an investor-style report.

### Key Assumptions

- Annual data is enough for a first-pass review.
- Ratios are interpreted directionally and should later be benchmarked against peers.
- Fake sample data is educational and not tied to actual investment advice.

### Output / Recommendation

The generated report summarizes revenue trends, profitability, liquidity, leverage, key risks, and a final financial health conclusion.

Report: `practical-projects/01-financial-statement-analysis/outputs/reports/financial_statement_analysis_report.md`

### What This Proves

Accounting fluency, ratio analysis, financial interpretation, charting, and concise executive summary writing.

## 3. Python Portfolio Analysis

Project folder: [02-python-portfolio-analysis](practical-projects/02-python-portfolio-analysis/README.md)

### Problem

Evaluate how a sample portfolio performed and what risks it carried across return, volatility, drawdown, allocation, and correlation.

### Data / Source Used

Fake daily stock price data and portfolio weights stored in CSV files.

### Method

Calculated daily returns, weighted portfolio returns, cumulative returns, annualized volatility, Sharpe ratio, max drawdown, asset-level risk-return, and correlation matrix.

### Key Assumptions

- Weights are normalized to sum to 100%.
- Risk-free rate is fixed for the Sharpe ratio calculation.
- The short fake sample period is useful for learning but not stable enough for real allocation decisions.

### Output / Recommendation

The generated report explains portfolio return, allocation, risk, Sharpe ratio, drawdown, diversification, and limitations.

Report: `practical-projects/02-python-portfolio-analysis/outputs/reports/portfolio_analysis_report.md`

### What This Proves

Portfolio math, Python time-series analysis, risk communication, and visual portfolio diagnostics.

## 4. Credit Risk Analysis

Project folder: [03-credit-risk-analysis](practical-projects/03-credit-risk-analysis/README.md)

### Problem

Classify borrower risk and explain why certain borrowers appear safer or riskier.

### Data / Source Used

Fake borrower data with income, debt-to-income, credit history, missed payments, existing debt, employment status, loan amount, and sample default flag.

### Method

Created a transparent rule-based credit score, estimated default probability, assigned risk categories, summarized segments, and generated borrower examples.

### Key Assumptions

- The model is rule-based and designed for learning.
- Debt-to-income, missed payments, unemployment, and loan pressure are major risk drivers.
- Real credit models require validation, calibration, fairness testing, and compliance review.

### Output / Recommendation

The generated report summarizes risk segments, key drivers, safest borrowers, riskiest borrowers, limitations, and final model-use conclusion.

Report: `practical-projects/03-credit-risk-analysis/outputs/reports/credit_risk_analysis_report.md`

### What This Proves

Risk modeling logic, probability framing, borrower segmentation, ethical limitation writing, and practical credit analysis.

## Supporting CLI Projects

The smaller projects in `projects/` are useful supporting artifacts:

- Black-Scholes option pricing and implied volatility.
- CAPM beta and expected return.
- APT factor expected return.
- Event-study abnormal returns.
- Limits-to-arbitrage risk score.
- Governance risk flags.
- Simple portfolio optimizer.

## Disclaimer

All outputs are for educational purposes only and are not investment advice, lending advice, or a recommendation to buy, sell, lend, borrow, or trade.

