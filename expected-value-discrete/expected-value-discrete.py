import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    return float(sum(xi * pi for xi , pi in zip(x, p)))
    pass