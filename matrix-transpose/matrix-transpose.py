import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    m = len(A)
    n = len(A[0])
    sol = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            sol[j][i] = A[i][j]

    return np.array(sol)

