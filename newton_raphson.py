# Newton-Raphson method

import math
import numpy as np

def f(x):
    return (math.e ** (- x)) - x

def f_prime(x):
    return (-math.e ** (-x)) - 1

x_prev = float(input('Insert starting point: '))
programmed_error = float(input('Insert programmed error: '))
i = 0
error = programmed_error + 1

print('i', 'xi', 'f(xi)', "f'(xi)", '|E|')
print(i, x_prev, f(x_prev), f_prime(x_prev), '-')

while programmed_error <= error:
    xi = x_prev - (f(x_prev) / f_prime(x_prev))
    f_xi = f(xi)
    f_prime_xi = f_prime(xi)
    error = abs(xi - x_prev)
    i += 1
    x_prev = xi
    print(i, xi, f(xi), f_prime(xi), error)

# Secant method

def f(x):
    return (math.e ** (- x)) - x

x_prev = float(input('Insert starting point: '))
programmed_error = float(input('Insert programmed error: '))
i = 0
error = programmed_error + 1

print('i', 'xi', 'f(xi)', '|E|')
print(i, x_prev, f(x_prev), '-')

while programmed_error <= error:
    xi = x_prev - ((f(x_prev))*() / f_prime(x_prev))
    f_xi = f(xi)
    error = abs(xi - x_prev)
    i += 1
    x_prev = xi
    print(i, xi, f(xi), f_prime(xi), error)