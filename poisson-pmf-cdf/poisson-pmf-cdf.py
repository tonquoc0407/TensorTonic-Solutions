import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    def calc_pmf(i: int) -> float:
        return (math.exp(-lam)* (lam ** i)) / math.factorial(i)
    pmf_val = calc_pmf(k)

    cdf_val = sum(calc_pmf(i) for i in range (k+1))

    return {
        "pmf": pmf_val,
        "cdf": cdf_val
    }
    pass