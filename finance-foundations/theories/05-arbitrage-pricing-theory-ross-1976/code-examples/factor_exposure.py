"""One-factor exposure."""
def mean(values):
    return sum(values) / len(values)

def factor_exposure(asset, factor):
    am, fm = mean(asset), mean(factor)
    cov = sum((a - am) * (f - fm) for a, f in zip(asset, factor))
    var = sum((f - fm) ** 2 for f in factor)
    if var == 0:
        raise ValueError("factor variance cannot be zero")
    return cov / var

if __name__ == "__main__":
    print(factor_exposure([0.03, -0.01, 0.04], [0.02, -0.02, 0.03]))
