"""APT-style factor model."""
def apt_expected_return(rf, exposures, premiums):
    return rf + sum(b * p for b, p in zip(exposures, premiums))
if __name__ == "__main__":
    exposures = [1.1, -0.3, 0.4]
    premiums = [0.05, 0.01, 0.02]
    print({"exposures": exposures, "expected_return": round(apt_expected_return(0.03, exposures, premiums), 4)})
