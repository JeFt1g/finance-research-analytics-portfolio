"""Basic Black-Scholes Greeks."""
from math import exp, pi, sqrt
from black_scholes import d1, d2, normal_cdf

def normal_pdf(x):
    return exp(-0.5 * x * x) / sqrt(2 * pi)

def delta(option_type, spot, strike, rate, time, volatility):
    value = normal_cdf(d1(spot, strike, rate, time, volatility))
    return value if option_type == "call" else value - 1

def gamma(spot, strike, rate, time, volatility):
    return normal_pdf(d1(spot, strike, rate, time, volatility)) / (spot * volatility * sqrt(time))

def vega(spot, strike, rate, time, volatility):
    return spot * normal_pdf(d1(spot, strike, rate, time, volatility)) * sqrt(time)

if __name__ == "__main__":
    print(delta("call", 100, 105, 0.04, 0.5, 0.25), gamma(100, 105, 0.04, 0.5, 0.25), vega(100, 105, 0.04, 0.5, 0.25))
