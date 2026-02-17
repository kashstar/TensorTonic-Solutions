import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    xarr = np.array(x)
    return 1/(1 + np.exp(-xarr))