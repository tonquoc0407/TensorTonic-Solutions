import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X_arr = np.array(X, dtype=float)
    n, d = X_arr.shape
    mu = np.mean(X_arr, axis=0)
    X_c = X_arr - mu

    C = (X_c.T @ X_c) / (n - 1)

    eigenvalues, eigenvectors = np.linalg.eig(C)
    # change to real for smallest diff
    eigenvalues = np.real(eigenvalues)
    eigenvectors = np.real(eigenvectors)

    sorted_indices = np.argsort(eigenvalues)[::-1] # argsort rev with ::-1

    W = eigenvectors[:, sorted_indices][:, :k]

    X_proj = X_c @ W

    return X_proj.tolist()
    pass