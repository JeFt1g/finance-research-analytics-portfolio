# Portfolio Submission Checklist

## Ready

- [x] Portfolio entry point exists: `PORTFOLIO.md`.
- [x] Career portfolio page exists: `CAREER_PORTFOLIO.md`.
- [x] Standardized project one-pagers exist: `PROJECT_ONE_PAGERS.md`.
- [x] Root README links to portfolio work.
- [x] Root index includes the practical project lab.
- [x] Root index includes the compact CLI project group.
- [x] Resume, contact, writing sample, and pitch deck placeholders exist.
- [x] Every project has a README.
- [x] Every practical project has sample data.
- [x] Every practical project generates a report.
- [x] Every practical project generates chart PNGs.
- [x] Every legacy CLI project runs with `python main.py`.
- [x] No project requires paid market data APIs.
- [x] Educational and fake-data limitations are documented.
- [x] Automated portfolio verifier passes.

## Reviewer Path

1. Open `PORTFOLIO.md`.
2. Open `CAREER_PORTFOLIO.md`.
3. Review `PROJECT_ONE_PAGERS.md`.
4. Review the four practical projects first.
5. Open each generated report under `practical-projects/*/outputs/reports/`.
6. Inspect charts under `practical-projects/*/outputs/charts/`.
7. Run `scripts/check_portfolio.py` for a reproducibility check.

## Verification Command

```powershell
cd "C:\Users\User\Documents\Projects (Finance)\finance-foundations"
.\practical-projects\.venv\Scripts\python scripts\check_portfolio.py
```

Verified result:

- 7 legacy CLI projects passed.
- 4 practical report/chart projects passed.
- 19 practical project charts found.
- Portfolio check passed.

## Personal Items To Replace Before Public Sharing

- [ ] Replace `[Your Name]`, school, graduation date, target roles, email, and links.
- [ ] Add final resume PDF under `portfolio-assets/resume/`.
- [ ] Add real LinkedIn URL.
- [ ] Add professional email.
- [ ] Add screenshots or exported PDFs if submitting outside GitHub.

## Final Polish Still Worth Doing Later

- Add screenshots to the root portfolio page.
- Convert the CLI examples into unit tests.
- Add a small Streamlit or static dashboard for the practical projects.
- Replace fake sample data with public SEC or market data loaders where appropriate.
