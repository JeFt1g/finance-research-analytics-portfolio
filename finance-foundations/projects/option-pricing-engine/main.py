"""CLI option pricing engine."""
import argparse
from math import erf, exp, log, sqrt

def n(x): return 0.5 * (1 + erf(x / sqrt(2)))
def d1(s, k, r, t, v): return (log(s / k) + (r + 0.5 * v * v) * t) / (v * sqrt(t))
def price(kind, s, k, r, t, v):
    a = d1(s, k, r, t, v)
    b = a - v * sqrt(t)
    if kind == "call": return s * n(a) - k * exp(-r * t) * n(b)
    return k * exp(-r * t) * n(-b) - s * n(-a)
def implied_vol(target, kind, s, k, r, t):
    low, high = 0.0001, 5
    for _ in range(100):
        mid = (low + high) / 2
        if price(kind, s, k, r, t, mid) < target: low = mid
        else: high = mid
    return (low + high) / 2
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--type", choices=["call", "put"], default="call")
    p.add_argument("--spot", type=float, default=100)
    p.add_argument("--strike", type=float, default=105)
    p.add_argument("--rate", type=float, default=0.04)
    p.add_argument("--time", type=float, default=0.5)
    p.add_argument("--volatility", type=float, default=0.25)
    p.add_argument("--market-price", type=float)
    a = p.parse_args()
    print("price", round(price(a.type, a.spot, a.strike, a.rate, a.time, a.volatility), 4))
    if a.market_price: print("implied_volatility", round(implied_vol(a.market_price, a.type, a.spot, a.strike, a.rate, a.time), 4))
if __name__ == "__main__": main()
