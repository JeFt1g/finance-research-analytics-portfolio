# Finance Foundations

## One-Sentence Summary

A finance research and analytics portfolio combining foundational theory, article analysis, and executable Python finance apps.

## What Is Inside

- Seven foundational finance theory folders
- A local article research system
- A rule-based article reader for `.txt`, `.md`, and optional `.pdf`
- Four practical finance analytics projects
- Streamlit dashboards for research and project review
- Sample data, generated charts, markdown reports, and case studies
- Portfolio presentation files for GitHub and resume use

## How To Use This Repo

1. Read the theory folders under `theories/`.
2. Process sample articles with `shared/article_reader/article_reader.py`.
3. Run the four apps in `practical-projects/`.
4. Review generated reports and charts.
5. Use `PORTFOLIO.md` and project case studies for portfolio presentation.

## Research System

The research system lives in `research/`. Add articles to `research/articles/`, process them with the article reader, then connect useful insights to theory folders and practical projects.

## Practical Apps

| Project | CLI Command | Output |
|---|---|---|
| Financial Statement Analysis | `cd practical-projects/01-financial-statement-analysis && python main.py` | Ratios, charts, and financial statement report |
| Python Portfolio Analysis | `cd practical-projects/02-python-portfolio-analysis && python main.py` | Returns, volatility, Sharpe ratio, drawdown, and correlation report |
| Credit Risk Analysis | `cd practical-projects/03-credit-risk-analysis && python main.py` | Borrower scoring, default probability, and risk segment report |
| Stock Valuation | `cd practical-projects/04-stock-valuation-dcf-comparables && python main.py` | DCF, comparables, sensitivity, and recommendation report |

## Theory Knowledge Base

- `01-black-scholes-1973`
- `02-market-efficiency-fama-1970`
- `03-modern-portfolio-theory-markowitz-1952`
- `04-capm-sharpe`
- `05-arbitrage-pricing-theory-ross-1976`
- `06-agency-theory-jensen-meckling-1976`
- `07-limits-to-arbitrage-shleifer-vishny-1997`

## Installation

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

## How To Run

See `HOW_TO_RUN.md` for the full command list.

## Best Demo Order

1. Stock Valuation App
2. Portfolio Analysis App
3. Finance Research App
4. Financial Statement Analysis App
5. Credit Risk App

## Folder Structure

```text
theories/
research/
shared/
apps/
practical-projects/
projects/
portfolio-assets/
```

## Future Improvements

- Add real public-company filings
- Add benchmark and factor data imports
- Add PDF source citation extraction
- Add automated Streamlit screenshots
- Expand into AI finance agents with source-backed retrieval

## Existing Portfolio Assets

The earlier portfolio materials remain available in `CAREER_PORTFOLIO.md`, `PROJECT_ONE_PAGERS.md`, `SUBMISSION_CHECKLIST.md`, and `portfolio-assets/`.
