"""Implied volatility by bisection."""
from black_scholes import call_price, put_price

def implied_volatility(market_price, option_type, spot, strike, rate, time, low=0.0001, high=5.0):
    if market_price <= 0:
        raise ValueError("market_price must be positive")
    price_fn = call_price if option_type == "call" else put_price
    for _ in range(100):
        mid = (low + high) / 2
        model_price = price_fn(spot, strike, rate, time, mid)
        if abs(model_price - market_price) < 1e-6:
            return mid
        if model_price < market_price:
            low = mid
        else:
            high = mid
    return (low + high) / 2

if __name__ == "__main__":
    print(round(implied_volatility(8, "call", 100, 105, 0.04, 0.5), 4))
