# Finance CLI Projects

These are small theory-to-code projects. They are intentionally compact so the finance formulas stay visible and easy to inspect.

## Projects

| Project | Concept | What It Demonstrates |
|---|---|---|
| [Option Pricing Engine](option-pricing-engine/README.md) | Black-Scholes | Option price and implied volatility from core assumptions. |
| [Portfolio Optimizer](portfolio-optimizer/README.md) | Modern Portfolio Theory | Return, volatility, Sharpe ratio, and simple weight sweep. |
| [CAPM Beta Calculator](capm-beta-calculator/README.md) | CAPM | Beta and expected return from stock and market returns. |
| [Multifactor Model Lab](multifactor-model-lab/README.md) | APT | Expected return from factor exposures and premiums. |
| [Market Efficiency Tester](market-efficiency-tester/README.md) | EMH | Event-window abnormal returns and cumulative abnormal return. |
| [Mispricing Risk Dashboard](mispricing-risk-dashboard/README.md) | Limits to Arbitrage | Mispricing risk score from liquidity, borrow, volatility, and leverage. |
| [Corporate Governance Analyzer](corporate-governance-analyzer/README.md) | Agency Theory | Governance risk flags from disclosure-style text. |

## Run

Each project runs from its own folder:

```powershell
cd option-pricing-engine
python main.py
```

No external dependencies are required for these CLI projects.

## Portfolio Notes

Use these projects as supporting evidence that the theory notes connect to working code. The stronger, report-style portfolio pieces live in [../practical-projects](../practical-projects/README.md).

