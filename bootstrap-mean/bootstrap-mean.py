import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    arr = np.array(x)
    n = len(arr)

    rng = np.random.default_rng(seed)

    samples = rng.choice(arr, size=(n_bootstrap, n), replace=True)

    bootstrap_means = np.mean(samples, axis=1)

    b_mean = float(np.mean(bootstrap_means))

    alpha = (1.0 - ci) / 2.0
    lower_bound = float(np.quantile(bootstrap_means, alpha))
    upper_bound = float(np.quantile(bootstrap_means, 1.0 - alpha))

    return {
        "bootstrap_mean": b_mean,
        "lower": lower_bound,
        "upper": upper_bound
    }
    
    pass