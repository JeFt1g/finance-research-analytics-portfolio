"""APT expected return."""
def apt_expected_return(risk_free_rate, exposures, premiums):
    if len(exposures) != len(premiums):
        raise ValueError("inputs must match")
    return risk_free_rate + sum(b * f for b, f in zip(exposures, premiums))

if __name__ == "__main__":
    print(apt_expected_return(0.03, [1.1, -0.4, 0.2], [0.05, 0.01, 0.03]))
