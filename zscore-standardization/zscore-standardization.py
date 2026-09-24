import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    arr = np.array(X, dtype=float)
    mu = np.mean(arr, axis=axis, keepdims=True)
    sigma = np.std(arr, axis=axis, ddof=0, keepdims=True)
    sigma_safe = np.where(sigma <= eps, 1.0, sigma)
    z = (arr - mu) / sigma_safe
    z_final = np.where(sigma <= eps, 0.0, z)
    return z_final
    pass