import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here
    arr = np.array(X, dtype=float)

    with np.errstate(all='ignore'):
        if strategy == "median":
            stats = np.nanmedian(arr, axis=0)
        else:
            stats = np.nanmean(arr, axis=0)
    stats = np.nan_to_num(stats, nan=0.0)
    imputed_arr = np.where(np.isnan(arr), stats, arr)
    
    return imputed_arr
    pass