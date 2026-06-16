"""CAPM alpha."""
from capm_expected_return import capm_expected_return

def alpha(actual, risk_free_rate, beta, market_return):
    return actual - capm_expected_return(risk_free_rate, beta, market_return)

if __name__ == "__main__":
    print(alpha(0.12, 0.04, 1.2, 0.09))
