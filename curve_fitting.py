# curve fitting

# linear least squares

import numpy as np

n = 7                                               # number of points (xi, yi)

xi = []
yi = [0.50, 2.50, 2.00, 4.00, 3.50, 6.00, 5.50]
xi_square = []
xi_yi = []

for i in range(1, n + 1):
    xi.append(i)
    xi_square.append(xi[i-1] ** 2)
    xi_yi.append(xi[i-1] * yi[i-1])

print(xi)
print(yi)
print(xi_square)
print(xi_yi)

print(sum(xi))
print(sum(yi))
print(sum(xi_square))
print(sum(xi_yi))

a1 = ((n * sum(xi_yi) - sum(xi) * sum(yi)) / (n * sum(xi_square) - (sum(xi)) ** 2))
a0 = np.mean(yi) - a1 * np.mean(xi)

print('a1 = {}'.format(a1))
print('a0 = {}'.format(a0))
