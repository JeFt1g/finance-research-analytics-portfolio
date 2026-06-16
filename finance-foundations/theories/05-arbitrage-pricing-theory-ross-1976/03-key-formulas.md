# Arbitrage Pricing Theory Ross 1976 - Key Formulas

## One-Sentence Summary

APT models expected return as compensation for exposure to multiple risk factors.

## Why It Matters

It expands CAPM's one-beta view into a flexible factor framework closer to modern risk systems.

## Core Idea

These are the formulas and framework pieces most likely to become code.

## Key Terms

- Factor
- Factor exposure
- Factor risk premium
- Macro factor
- Inflation
- Interest rates
- Credit spreads
- No-arbitrage

## Formula / Model

```txt
Expected Return = Risk-Free Rate + b1*F1 + b2*F2 + ... + bn*Fn
Return = alpha + b1*factor1 + ... + residual
```

## Simple Example

A bank stock can be exposed to the broad market, interest rates, credit spreads, and economic growth at the same time.

## Real-World Use

Hedge fund risk models, factor investing, macro dashboards, performance attribution, and exposure controls.

## Limitations

- APT does not tell you exactly which factors to use.
- Factor exposures can be unstable.
- Correlated factors can create false precision.

## Project Ideas

- Multi-factor stock model
- Factor exposure calculator
- Macro sensitivity dashboard
- CAPM vs APT comparison tool

## Links To Other Theories

- [CAPM](../04-capm-sharpe/README.md)
- [MPT](../03-modern-portfolio-theory-markowitz-1952/README.md)
- [Market Efficiency](../02-market-efficiency-fama-1970/README.md)

## Coding Checklist

- Keep variables named after the formula.
- Check time units and return periods.
- Handle invalid inputs.
- Add one sample run.
