# Black-Scholes 1973 - Summary

## One-Sentence Summary

Black-Scholes prices European options from spot price, strike, time, rates, and volatility.

## Why It Matters

It turned option pricing from dealer intuition into a repeatable model for quoting, hedging, and building derivatives software.

## Core Idea

Black-Scholes prices European options from spot price, strike, time, rates, and volatility. Use it when the project needs options calculators, greeks dashboards, market-making tools, implied volatility solvers, and strategy visualizers.

## Key Terms

- Option
- Call
- Put
- Strike
- Risk-free rate
- Volatility
- Implied volatility
- Delta
- Put-call parity

## Formula / Model

```txt
Call = S*N(d1) - K*exp(-rT)*N(d2)
Put  = K*exp(-rT)*N(-d2) - S*N(-d1)
d1 = [ln(S/K) + (r + sigma^2/2)T] / [sigma*sqrt(T)]
d2 = d1 - sigma*sqrt(T)
Put-call parity: C - P = S - K*exp(-rT)
```

## Simple Example

A one-year at-the-money call is worth more at 40% volatility than at 15% volatility because the upside tail becomes more valuable.

## Real-World Use

Options calculators, Greeks dashboards, market-making tools, implied volatility solvers, and strategy visualizers.

## Limitations

- Assumes European exercise and frictionless continuous hedging.
- Assumes constant volatility and rates.
- Can break down during jumps, crashes, liquidity stress, and volatility regime shifts.

## Project Ideas

- Option pricing calculator
- Implied volatility solver
- Greeks dashboard
- Options strategy visualizer

## Links To Other Theories

- [MPT](../03-modern-portfolio-theory-markowitz-1952/README.md)
- [CAPM](../04-capm-sharpe/README.md)
- [Limits to Arbitrage](../07-limits-to-arbitrage-shleifer-vishny-1997/README.md)

## Memory Hook

Black-Scholes prices European options from spot price, strike, time, rates, and volatility.
