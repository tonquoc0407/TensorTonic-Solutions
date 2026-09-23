import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here

    A_array = np.array(A, dtype = float)
    n = A_array.shape[0]

    I = np.eye(n, dtype = float)
    aug = np.hstack((A_array, I))

    for i in range(n):
        max_row_idx = i + np.argmax(np.abs(aug[i:, i]))

        # if biggest pivot = 0
        if np.isclose(aug[max_row_idx, i], 0.0):
            return None

        # change the position of current row with row having biggest pivot
        if max_row_idx != i:
            aug[[i, max_row_idx]] = aug[[max_row_idx, i]]

        aug[i] = aug[i] / aug[i, i]

        for j in range(n):
            if i != j:
                aug[j] -= aug[j, i] * aug[i]
    return aug[ :, n:]
    pass