"""Compare CAPM and APT."""
from apt_model import apt_expected_return

def capm(rf, beta, market):
    return rf + beta * (market - rf)

if __name__ == "__main__":
    print({"capm": capm(0.03, 1.1, 0.09), "apt": apt_expected_return(0.03, [1.0, -0.2], [0.05, 0.01])})
