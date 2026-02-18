import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    dot = np.dot(a,b)
    a1 = np.linalg.norm(a)
    b1 = np.linalg.norm(b)

    if a1 == 0  or b1 == 0:
        return 0.0
    else:
        return dot/(a1*b1)
    pass