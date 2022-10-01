import numpy as np

# A * x = B
# how to create a m x n matrix

a11, a12, a13 = 2, 4, 3
a21, a22, a23 = -1, 3, 4
a31, a32, a33 = -5, 5, 4

A = np.array([[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]], dtype=np.float64)

print(A.shape)

b1, b2, b3 = 2, 4, -1

B = np.array([b1, b2, b3])

print(A)
print(type(A))

print(B)
print(type(B))

def triangular(matrix):
    """
    A | B
    matrix: matriz extendida a triangular
    Triangula la matriz "matrix"
    """
    shape = matrix.shape
    for i in range(shape[0]-1):
        a = matrix[i][i]
        for j in range(i+1, shape[0]):
            n = matrix[j][i]
            m = n/a
            matrix[j] -= matrix[i] * m

triangular(A)
print(A)