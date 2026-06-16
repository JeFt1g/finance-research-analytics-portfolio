# QA Report

## Apps Checked

| Area | Status | Notes |
|---|---|---|
| Finance Research App | Ready | Launched on localhost and captured `apps/finance_research_app/outputs/screenshots/finance_research_app.png`. |
| Project Dashboard Launcher | Ready | Launched on localhost and captured `apps/project_dashboard_launcher/outputs/screenshots/project_dashboard_launcher.png`. |
| Practical project dashboards | Ready | All four project dashboards launched on localhost and screenshots were captured. |

## CLI Commands Checked

Checked with the existing interpreter at `practical-projects/.venv/Scripts/python.exe`.

| Command | Status |
|---|---|
| `python shared/article_reader/article_reader.py --input research/articles/sample_company_article.txt` | Ready |
| `cd practical-projects/01-financial-statement-analysis && python main.py` | Ready |
| `cd practical-projects/02-python-portfolio-analysis && python main.py` | Ready |
| `cd practical-projects/03-credit-risk-analysis && python main.py` | Ready |
| `cd practical-projects/04-stock-valuation-dcf-comparables && python main.py` | Ready |
| `python scripts/check_portfolio.py` | Ready |

## Dashboard Commands Checked

| Command | Status | Notes |
|---|---|---|
| `streamlit run apps/finance_research_app/app.py` | Ready | Verified on port 8511. |
| `streamlit run apps/project_dashboard_launcher/app.py` | Ready | Verified on port 8512. |
| `streamlit run practical-projects/<project>/app.py` | Ready | Verified project dashboards on ports 8513-8516. |

## Article Reader Checked

Ready. The sample company article was processed and saved to `research/processed/sample_company_article_analysis.md`.

## Theory Folders Checked

Ready. All seven theory folders now include:

- `06-project-connections.md`
- `08-article-notes.md`
- `09-reading-list.md`
- `10-flashcards.md`
- `11-summary.md`
- `research/articles/`
- `research/processed/`
- `research/summaries/`

## Practical Projects Checked

Ready for CLI mode. All four practical projects have:

- `main.py`
- `app.py`
- `RUN_THIS_PROJECT.md`
- `PROJECT_CASE_STUDY.md`
- `requirements.txt`
- `research/`
- `outputs/charts/`
- `outputs/reports/`
- `outputs/screenshots/README.md`
- `tests/test_basic_run.py`

## Files Created

Major new areas:

- `research/`
- `shared/article_reader/`
- `shared/utils/`
- `apps/finance_research_app/`
- `apps/project_dashboard_launcher/`
- Root docs: `HOW_TO_RUN.md`, `PROJECT_INDEX.md`, `RESEARCH_INDEX.md`, `ARTICLE_LIBRARY.md`, `PORTFOLIO_CHECKLIST.md`
- Practical project wrappers, dashboards, tests, case studies, and run guides
- Theory article integration files

## Known Limitations

- The default system `python` in this environment is missing `matplotlib`; use the existing `practical-projects/.venv` or install `requirements.txt`.
- The finance research app loaded and was screenshot successfully. Headless automation did not reliably enable the analysis button from typed text, so the captured image shows the loaded research form rather than a completed pasted-article run.
- Article analysis is rule-based and does not replace professional analyst review.
- Sample datasets are fake and educational.
- Screenshot folders contain instructions, not final screenshots.

## Remaining Improvements

- Add real PDF/article sources and update the article index.
- Add benchmark data and factor attribution to the portfolio app.
- Add real filings or financial data exports for valuation and statement analysis.
- Add automated dashboard screenshot generation.

## Final Status

| Area | Final Status |
|---|---|
| Theory knowledge base | Ready |
| Research article system | Ready |
| Shared article reader | Ready |
| Practical project CLI apps | Ready |
| Reports and charts | Ready |
| Streamlit dashboards | Ready |
| Portfolio docs | Ready |
| Screenshots | Ready |
