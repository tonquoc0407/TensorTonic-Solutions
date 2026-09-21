from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    gonna try using pythonic solving ways only, no focused on numpy
    """
    n = len(x)

    mean_val = sum(x) / n

    x_sorted = sorted(x)
    mid = n // 2
    if n % 2 == 0:
        median_val = (x_sorted[mid - 1] + x_sorted[mid]) / 2
    else:
        median_val = float(x_sorted[mid])

    freq_x = Counter(x)
    max_freq = max(freq_x.values())

    mode_val = float(min(k for k, v in freq_x.items() if v == max_freq))

    return {
        "mean": float(mean_val),
        "median": float(median_val),
        "mode": float(mode_val)
    }
    
    pass