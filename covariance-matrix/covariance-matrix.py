import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X_arr = np.array(X)
    N = X_arr.shape[0]
    mu = np.mean(X_arr, axis=0)
    X_c = X_arr - mu

    cov_matrix = (X_c.T @ X_c) / (N - 1)
    
    return cov_matrix
    
    pass