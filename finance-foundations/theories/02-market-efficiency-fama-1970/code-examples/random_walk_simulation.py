"""Random walk price simulation."""
import random

def random_walk(start=100.0, periods=20, step=0.02, seed=7):
    random.seed(seed)
    prices = [start]
    for _ in range(periods):
        prices.append(prices[-1] * (1 + random.choice([-step, step])))
    return prices

if __name__ == "__main__":
    print([round(x, 2) for x in random_walk()])
