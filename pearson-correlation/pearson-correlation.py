import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X_arr = np.array(X, dtype=float)
    N = X_arr.shape[0]

    mu = np.mean(X_arr, axis = 0)

    X_c = X_arr - mu 
    cov_matrix = (X_c.T @ X_c) / (N - 1)

    variances = np.diag(cov_matrix)
    std_devs = np.sqrt(variances)

    # np.outer(A,B)
    denominator = np.outer(std_devs, std_devs)

    correlation_matrix = np.where(
        denominator == 0,
        np.nan,
        cov_matrix / denominator 
    )

    return correlation_matrix
    
    pass