# curve fitting

# linear least squares
import math

import numpy as np

def linear_least_squares(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                               # number of points (xi, yi)
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

def exponential_model(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                             # number of points (xi, yi)
        ln_yi = []
        xi_square = []
        xi_ln_yi = []
        for i in range(1, n + 1):
            ln_yi.append(np.log(yi[i - 1]))
            xi_square.append(xi[i - 1] ** 2)
            xi_ln_yi.append(xi[i - 1] * ln_yi[i - 1])
        print('xi: {}'.format(xi))
        print('yi: {}'.format(yi))
        print('lnyi: {}'.format(ln_yi))
        print('xi square: {}'.format(xi_square))
        print('xiyi: {}'.format(xi_ln_yi))

        print('Sum xi = {}'.format(sum(xi)))
        print('Sum lnyi = {}'.format(sum(ln_yi)))
        print('Sum xi square = {}'.format(sum(xi_square)))
        print('Sum xilnyi = {}'.format(sum(xi_ln_yi)))

        a1 = ((n * sum(xi_ln_yi) - sum(xi) * sum(ln_yi)) / (n * sum(xi_square) - (sum(xi)) ** 2))
        a0 = np.mean(ln_yi) - a1 * np.mean(xi)

        A = math.e ** a0                # y = A.e**(B.x)
        B = a1

        print('a0 = {}'.format(a0))
        print('a1 = B = {}'.format(a1))
        print('A = {}'.format(A))

        print('y = {} . e**{}x'.format(A, B))
    else:
        print('Error')


if __name__ == '__main__':
    xi_lls = [1, 2, 3, 4, 5, 6, 7]
    yi_lls = [0.50, 2.50, 2.00, 4.00, 3.50, 6.00, 5.50]
    linear_least_squares(xi_lls, yi_lls)

    xi_exp = [1, 2, 3, 4, 5]
    yi_exp = [0.5, 1.7, 3.4, 5.7, 8.4]
    exponential_model(xi_exp, yi_exp)