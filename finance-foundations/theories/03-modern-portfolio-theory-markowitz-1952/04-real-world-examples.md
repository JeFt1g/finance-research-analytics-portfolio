# Modern Portfolio Theory Markowitz 1952 - Real-World Examples

## One-Sentence Summary

MPT says portfolio risk depends on weights, volatility, and correlation, not just individual asset risk.

## Why It Matters

It is the foundation for diversification, asset allocation, efficient frontiers, and risk-aware portfolio software.

## Core Idea

- why uncorrelated assets matter
- stocks and bonds
- tech stocks vs utilities
- why concentration can be dangerous

## Key Terms

- Expected return
- Variance
- Standard deviation
- Correlation
- Covariance
- Diversification
- Efficient frontier
- Sharpe ratio

## Formula / Model

```txt
Portfolio return = sum(w_i*r_i)
Two-asset variance = w1^2*s1^2 + w2^2*s2^2 + 2*w1*w2*rho*s1*s2
Multi-asset variance = w^T*Sigma*w
Sharpe = (return - risk-free rate) / volatility
```

## Simple Example

A mix of stocks and high-quality bonds can be less volatile than a stock-only portfolio if their returns are not highly correlated.

## Real-World Use

Robo-advisors, retirement allocation, efficient frontier tools, risk dashboards, and institutional portfolio construction.

## Limitations

- Expected returns and correlations are noisy estimates.
- Correlations can rise during market stress.
- Unconstrained optimization can produce extreme weights.

## Project Ideas

- Portfolio optimizer
- Efficient frontier visualizer
- Risk contribution analyzer
- Asset allocation simulator

## Links To Other Theories

- [CAPM](../04-capm-sharpe/README.md)
- [APT](../05-arbitrage-pricing-theory-ross-1976/README.md)
- [Black-Scholes](../01-black-scholes-1973/README.md)

## Example To Test Conversion

Turn each example into inputs, expected direction, and one limitation.
