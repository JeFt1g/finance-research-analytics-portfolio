"""Two-asset efficient frontier."""
from portfolio_return import portfolio_return
from portfolio_variance import two_asset_variance

def frontier(step=0.25):
    points = []
    for i in range(int(1 / step) + 1):
        w1 = i * step
        w2 = 1 - w1
        points.append((w1, portfolio_return([w1, w2], [0.08, 0.03]), two_asset_variance(w1, w2, 0.18, 0.07, 0.2) ** 0.5))
    return points

if __name__ == "__main__":
    print(frontier())
