# Newton-Raphson method

import math
import numpy as np

def f(x):
    return (math.e ** (- x)) - x

def f_prime(x):
    return (-math.e ** (-x)) - 1

xi = float(input('Insert starting point: '))
programmed_error = float(input('Insert programmed error: '))
i = 0
error = programmed_error + 1

print('i', 'xi', 'f(xi)', "f'(xi)", '|E|')
print(i, xi, f(xi), f_prime(xi), '-')

while programmed_error <= error:
    x_next = xi - (f(xi) / f_prime(xi))
    error = abs(x_next - xi)
    xi = x_next
    f_xi = f(xi)
    f_prime_xi = f_prime(xi)
    i += 1
    print(i, xi, f(xi), f_prime(xi), error)

# Secant method

import math

def f(x):
    return (math.e ** (- x)) - x

x_prev = float(input('Insert first point: '))
xi = float(input('Insert second point: '))
programmed_error = float(input('Insert programmed error: '))
i = 0
error = programmed_error + 1

print('i', 'xi', 'f(xi)', '|E|')
print(i, x_prev, f(x_prev), '-')
i += 1                                  # for loop to improve this part
print(i, xi, f(xi), '-')

while programmed_error <= error:
    x_next = xi - (f(xi) * (x_prev - xi)) / (f(x_prev) - f(xi))
    error = abs(x_next - xi)
    x_prev = xi
    xi = x_next
    f_xi = f(xi)
    i += 1
    print(i, xi, f(xi), error)