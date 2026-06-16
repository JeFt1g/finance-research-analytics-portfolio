"""Portfolio variance."""
def two_asset_variance(w1, w2, vol1, vol2, corr):
    return w1*w1*vol1*vol1 + w2*w2*vol2*vol2 + 2*w1*w2*corr*vol1*vol2

def matrix_variance(weights, cov):
    return sum(weights[i] * weights[j] * cov[i][j] for i in range(len(weights)) for j in range(len(weights)))

if __name__ == "__main__":
    print(two_asset_variance(0.6, 0.4, 0.18, 0.07, 0.2) ** 0.5)
