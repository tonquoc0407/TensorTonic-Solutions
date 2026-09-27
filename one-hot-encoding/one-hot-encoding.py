import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y_arr = np.array(y)
    n = len(y_arr)

    if n == 0:
        return np.array([[]], dtype = float)

    if num_classes is None:
        k = int(np.max(y_arr) +1 )
    else:
        k = num_classes
    matrix = np.zeros((n, k), dtype=float)

    matrix[np.arange(n), y_arr] = 1.0

    return matrix
    pass