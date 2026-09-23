import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    arr = np.array(x)

    n = len(arr)

    x_bar = np.mean(arr)

    s = np.std(arr, ddof = 1)

    if s == 0:
        if x_bar == mu0:
            return 0.0
        elif x_bar > mu0:
            return float('inf')
        elif x_bar < mu0:
            return float('-inf')

    t_stat = (x_bar - mu0) / (s / math.sqrt(n))

    return float(t_stat)
    pass
    