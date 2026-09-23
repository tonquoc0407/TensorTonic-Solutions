import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    A = np.array(matrix, dtype = float)
    eigen = np.linalg.eigvals(A)
    real_eigen = np.real(eigen)

    sort_eigen = np.sort(real_eigen)

    return sort_eigen
    pass