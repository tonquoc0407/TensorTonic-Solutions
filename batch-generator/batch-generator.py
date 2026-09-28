import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    X_arr = np.array(X)
    y_arr = np.array(y)

    n_samples = len(X_arr)
    rng = np.random.default_rng(seed)
    indices = np.arange(n_samples)
    rng.shuffle(indices)

    X_shuffled = X_arr[indices]
    y_shuffled = y_arr[indices]

    for i in range(0, n_samples, batch_size):
        X_batch = X_shuffled[i : i + batch_size]
        y_batch = y_shuffled[i : i + batch_size]
        if drop_last and len(X_batch) < batch_size:
            break
        yield (X_batch, y_batch)
    pass