import numpy as np
def print_matrix(M):
    print('M =')
    for i in range(len(M)):
        print('    ', end='')
        for j in range(len(M[0])):
            print(M[i][j], end='      ')
        print()
   
A = np.array([[2, 2, 3], [3, 1, 3], [3, 1, 3]])
print_matrix(A)