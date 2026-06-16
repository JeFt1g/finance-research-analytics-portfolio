"""CAPM expected return."""
def capm_expected_return(risk_free_rate, beta, market_return):
    return risk_free_rate + beta * (market_return - risk_free_rate)

if __name__ == "__main__":
    print(capm_expected_return(0.04, 1.2, 0.09))
