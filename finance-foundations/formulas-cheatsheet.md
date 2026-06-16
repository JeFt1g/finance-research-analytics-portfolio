# Formula Cheatsheet

## One-Sentence Summary

A practical cheat sheet for formulas used across the theory and project folders.

## Why It Matters

Most finance code bugs come from wrong units, mismatched periods, or misunderstood variables.

## Core Idea


### Black-Scholes Call Price

```txt
C = S*N(d1) - K*exp(-rT)*N(d2)
```
Variables: `S` stock price, `K` strike, `r` risk-free rate, `T` years, `sigma` volatility. Example: higher volatility raises option time value. Common mistake: mixing annual volatility with time measured in days.

### Black-Scholes Put Price

```txt
P = K*exp(-rT)*N(-d2) - S*N(-d1)
```
Example: a put gains value when downside protection becomes more valuable. Common mistake: ignoring time value.

### Portfolio Expected Return

```txt
E[R_p] = sum(w_i*E[R_i])
```
Example: 60% at 8% and 40% at 3% gives 6%. Common mistake: weights not summing to 1.

### Portfolio Variance

```txt
Variance = w^T*Sigma*w
```
Example: low-correlation assets can reduce volatility. Common mistake: averaging volatilities and ignoring covariance.

### Sharpe Ratio

```txt
Sharpe = (Return - Risk-Free Rate) / Volatility
```
Common mistake: comparing daily and annual Sharpe ratios without annualizing.

### CAPM Expected Return

```txt
E[R_i] = R_f + beta_i*(E[R_m] - R_f)
```
Example: 4% risk-free, 9% market, beta 1.2 gives 10%. Common mistake: treating historical return as guaranteed expected return.

### Beta

```txt
Beta = covariance(R_i, R_m) / variance(R_m)
```
Common mistake: mismatched return periods.

### APT Factor Model

```txt
E[R_i] = R_f + b1*F1 + b2*F2 + ... + bn*Fn
```
Common mistake: adding many correlated factors without interpretation.

### Jensen's Alpha

```txt
Alpha = R_actual - (R_f + beta*(R_m - R_f))
```
Common mistake: calling raw outperformance alpha before adjusting for beta.


## Key Terms

- S
- K
- r
- T
- sigma
- weight
- covariance
- beta
- alpha
- factor

## Formula / Model

Use consistent periods first, then implement the formula.

## Simple Example

Monthly stock returns should be compared with monthly market returns and monthly risk-free assumptions.

## Real-World Use

Use while coding pricing engines, optimizers, beta calculators, and factor models.

## Limitations

- Inputs are estimates.
- The formulas simplify real frictions.
- Different conventions can change outputs.

## Project Ideas

- Finance formula unit checker
- Formula tests
- Reusable math module

## Links To Other Theories

- [Black-Scholes](theories/01-black-scholes-1973/README.md)
- [MPT](theories/03-modern-portfolio-theory-markowitz-1952/README.md)
- [CAPM](theories/04-capm-sharpe/README.md)
