# curve fitting

# linear least squares

import numpy as np

def linear_least_squares(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                             # number of points (xi, yi)
        xi_square = []
        xi_yi = []
        for i in range(1, n + 1):
            xi_square.append(xi[i - 1] ** 2)
            xi_yi.append(xi[i - 1] * yi[i - 1])
        print('xi: {}'.format(xi))
        print('yi: {}'.format(yi))
        print('xi square: {}'.format(xi_square))
        print('xiyi: {}'.format(xi_yi))

        print('Sum xi = {}'.format(sum(xi)))
        print('Sum yi = {}'.format(sum(yi)))
        print('Sum xi square = {}'.format(sum(xi_square)))
        print('Sum xiyi = {}'.format(sum(xi_yi)))

        a1 = ((n * sum(xi_yi) - sum(xi) * sum(yi)) / (n * sum(xi_square) - (sum(xi)) ** 2))
        a0 = np.mean(yi) - a1 * np.mean(xi)

        print('a1 = {}'.format(a1))
        print('a0 = {}'.format(a0))

        print('y = {}x + {}'.format(a1, a0))
    else:
        print('Error')


# exponential model

# y = Ae ** Bx

n = 5

for i in range(1, n + 1):
    xi.append(i)
    xi_square.append(xi[i-1] ** 2)
    xi_yi.append(xi[i-1] * yi[i-1])


if __name__ == '__main__':
    xi = [1, 2, 3, 4, 5, 6, 7]
    yi = [0.50, 2.50, 2.00, 4.00, 3.50, 6.00, 5.50]
    linear_least_squares(xi, yi)