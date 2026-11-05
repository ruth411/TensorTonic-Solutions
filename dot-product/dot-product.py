import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    dot_product = float(sum(x*y for x,y in zip(x,y)))
    return dot_product
    pass
    print (dot_product(x,y))