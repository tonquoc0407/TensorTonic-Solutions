import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    arr = np.array(matrix, dtype=float)

    norm_type = str(norm_type).upper()
    if norm_type == "L1":
        ord_val = 1
    elif norm_type == "L2":
        ord_val = 2
    elif norm_type == "MAX":
        ord_val = np.inf
    else:
        ord_val = 2 # default is L2
    if axis is None:
        norm_val = np.linalg.norm(arr.flatten(), ord=ord_val)
        if norm_val == 0:
            return arr
        return arr / norm_val 

    norm_val = np.linalg.norm(arr, ord=ord_val, axis = axis, keepdims = True)

    norm_val_safe = np.where(norm_val == 0, 1.0, norm_val)

    return arr / norm_val_safe 
    
    pass