import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    arr = np.array(x)
    # calculating PMF for all array
    # if i = 1, replace with p, and reverse with 1 - p
    pmf_arr = np.where(arr == 1, p, 1 - p)

    mean_val = float(p)
    variance_val = float(p*(1-p))

    return {
        "pmf": pmf_arr, 
        "mean": mean_val, 
        "variance": variance_val
    }
    pass