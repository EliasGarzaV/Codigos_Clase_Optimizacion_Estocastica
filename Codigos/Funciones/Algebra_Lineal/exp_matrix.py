import numpy as np
from scipy.linalg import fractional_matrix_power
def exp_matrix(A, n):
    if(int(n) == n):
        return np.linalg.matrix_power(A, n)
    else:
        return fractional_matrix_power(A, n)


