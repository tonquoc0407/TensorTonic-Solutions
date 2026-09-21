import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    mean_x = sum(x) / n

    sum_sqr_diff = sum((xi - mean_x) ** 2 for xi in x)

    variance = sum_sqr_diff / (n-1)

    std_dev = math.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(std_dev)
    }
    pass