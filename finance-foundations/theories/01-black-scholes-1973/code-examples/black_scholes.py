"""Black-Scholes call and put pricing."""
from math import erf, exp, log, sqrt

def normal_cdf(x):
    return 0.5 * (1 + erf(x / sqrt(2)))

def d1(spot, strike, rate, time, volatility):
    if spot <= 0 or strike <= 0 or time <= 0 or volatility <= 0:
        raise ValueError("spot, strike, time, and volatility must be positive")
    return (log(spot / strike) + (rate + 0.5 * volatility ** 2) * time) / (volatility * sqrt(time))

def d2(spot, strike, rate, time, volatility):
    return d1(spot, strike, rate, time, volatility) - volatility * sqrt(time)

def call_price(spot, strike, rate, time, volatility):
    return spot * normal_cdf(d1(spot, strike, rate, time, volatility)) - strike * exp(-rate * time) * normal_cdf(d2(spot, strike, rate, time, volatility))

def put_price(spot, strike, rate, time, volatility):
    return strike * exp(-rate * time) * normal_cdf(-d2(spot, strike, rate, time, volatility)) - spot * normal_cdf(-d1(spot, strike, rate, time, volatility))

if __name__ == "__main__":
    print("call", round(call_price(100, 105, 0.04, 0.5, 0.25), 4))
    print("put", round(put_price(100, 105, 0.04, 0.5, 0.25), 4))
