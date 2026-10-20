import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    dot_prod = 0
    for a, b in zip(x, y):
        dot_prod += float(a*b)
    return dot_prod