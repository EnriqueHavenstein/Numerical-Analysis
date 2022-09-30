import numpy as np

a11, a12, a13 = 2, 4, 3
a21, a22, a23 = -1, 3, 4
a31, a32, a33 = -5, 5, 4

A = np.array([[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]])

print(A)
print(type(A))
