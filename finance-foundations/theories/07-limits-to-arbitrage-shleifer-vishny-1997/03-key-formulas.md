# Limits to Arbitrage Shleifer Vishny 1997 - Key Formulas

## One-Sentence Summary

Limits to Arbitrage explains why mispricings can persist even when rational traders see them.

## Why It Matters

It gives the practical layer missing from simple efficient-market stories: funding pressure, liquidity, short constraints, and forced exits.

## Core Idea

These are the formulas and framework pieces most likely to become code.

## Key Terms

- Mispricing
- Arbitrage
- Funding constraint
- Short-selling constraint
- Liquidity risk
- Career risk
- Investor withdrawals
- Short squeeze

## Formula / Model

```txt
Practical arbitrage return = convergence profit - financing cost - borrow cost - liquidity cost - forced-exit risk
Margin headroom = capital - required collateral after adverse move
```

## Simple Example

A fund shorts an overvalued stock, but the stock doubles before falling. If investors withdraw or lenders demand collateral, the fund may be forced out while still being right long term.

## Real-World Use

Short-squeeze dashboards, liquidity risk controls, hedge fund stress tests, mispricing trackers, and crowded trade analysis.

## Limitations

- Constraints are hard to observe before stress arrives.
- The theory explains persistence better than timing.
- Crowding, leverage, and liquidity can change quickly.

## Project Ideas

- Mispricing persistence tracker
- Short squeeze risk dashboard
- Liquidity risk model
- Arbitrage failure simulator

## Links To Other Theories

- [Market Efficiency](../02-market-efficiency-fama-1970/README.md)
- [Black-Scholes](../01-black-scholes-1973/README.md)
- [APT](../05-arbitrage-pricing-theory-ross-1976/README.md)

## Coding Checklist

- Keep variables named after the formula.
- Check time units and return periods.
- Handle invalid inputs.
- Add one sample run.
