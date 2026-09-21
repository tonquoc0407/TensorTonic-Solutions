import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    def cal_pmf(i: int) -> float:
        return math.comb(n, i) * (p**i) * ((1-p) ** (n - i))
    pmf_val = cal_pmf(k)
    cdf_val = sum(cal_pmf(i) for i in range(k+1))

    return {
        "pmf": float(pmf_val),
        "cdf": float(cdf_val)
    }
    pass