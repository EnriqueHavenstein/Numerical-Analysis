# Fixed point iteration

import math
import numpy as np
import sympy as sp

def f(x):
    return (math.e ** (- x)) - x

def g(x):
    return math.e ** (- x)

# def g_prime(x):
#      return g(x).diff(x)

# print(g_prime(2))
# x = sp.Symbol('x')
# y = x**2 + 1
# yprime = y.diff(x)
# print(yprime)

a = round(float(input('Insert a: ')), 4)
b = round(float(input('Insert b: ')), 4)
programmed_error = float(input('Insert programmed error: '))

if a < g(a) < b and a < g(b) < b:
    print('tut')
    # if |g_prime(E)| < 1
    # missing verification of g_prime()
    x = a
    g_x = g(x)
    print('xi', 'g(xi)', '|E|')
    print(x, g_x, '-')
    error = abs(b - a)
    while programmed_error <= error:
        x_prev = x
        x = g_x
        g_x = g(x)
        error = abs(x - x_prev)
        print(x, g_x, error)
else:
    print('g(x) function does not converge for the proposed interval')