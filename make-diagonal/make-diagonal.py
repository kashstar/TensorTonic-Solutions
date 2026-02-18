import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    ans = np.zeros((n,n))
    for i in range(len(v)):
        for j in range(len(v)):
            if i == j:
                ans[i][j] = v[i]

    return ans
    pass
