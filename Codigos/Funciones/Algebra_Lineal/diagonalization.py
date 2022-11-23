import numpy as np
def diagonalization(A):
    vals, vec_mat = np.linalg.eig(A)
    return vec_mat, np.diag(vals), np.linalg.inv(vec_mat)

A = np.array([[2, 2], [1, 3]])
Q, D, Q_inv = diagonalization(A)

print('Diag:')
print(np.linalg.multi_dot([Q, D, Q_inv]))
