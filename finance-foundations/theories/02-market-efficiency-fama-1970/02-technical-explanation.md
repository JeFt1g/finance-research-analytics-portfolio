# Market Efficiency Fama 1970 - Technical Explanation

## One-Sentence Summary

Market efficiency says prices tend to incorporate available information, making consistent outperformance difficult.

## Why It Matters

It explains why passive investing matters, why public stock picking is hard, and why every strategy needs risk, cost, and luck checks.

## Core Idea

The Efficient Market Hypothesis is not the claim that prices are always correct. It says competition pushes available information into prices quickly enough that easy excess returns are hard to capture. The useful question is what information is already priced and what it costs to trade on a possible edge. Technical focus points: weak, semi-strong, and strong forms, why index funds became important, why public information gets priced quickly, how transaction costs change strategy results. In code, represent the model with small pure functions, explicit units, deterministic sample data, and clear error handling.

## Key Terms

- Weak-form efficiency
- Semi-strong-form efficiency
- Strong-form efficiency
- Public information
- Alpha
- Transaction costs
- Luck vs skill
- Index investing

## Formula / Model

```txt
Abnormal Return = Stock Return - Benchmark Return
Cumulative Abnormal Return = sum(Abnormal Returns)
Net Alpha = Gross Excess Return - Costs - Risk Adjustment
```

## Simple Example

If strong earnings are released before the open, the stock may gap up immediately. A trader reading the same news later may not have an easy remaining profit.

## Real-World Use

Event studies, active manager evaluation, passive benchmark design, strategy testing, and news-reaction backtests.

## Limitations

- Markets can be inefficient when information is complex, costly, ignored, or hard to trade.
- EMH does not mean prices are always correct.
- Backtests can confuse luck, overfitting, and survivorship bias for skill.

## Project Ideas

- Market reaction tester
- News event backtester
- Active vs passive return analyzer
- Random stock-picking simulator

## Links To Other Theories

- [Limits to Arbitrage](../07-limits-to-arbitrage-shleifer-vishny-1997/README.md)
- [CAPM](../04-capm-sharpe/README.md)
- [MPT](../03-modern-portfolio-theory-markowitz-1952/README.md)
