# Bisection method

import math
import numpy as np

def f(x):
    return (math.e ** (- x)) - x

a = round(float(input('Insert a: ')), 4)
b = round(float(input('Insert b: ')), 4)
programmed_error = float(input('Insert programmed error: '))
chart = ['a', 'b', 'c', 'f(a)', 'f(c)', 'f(a)*f(c) > 0', 'Error']

c = round((a + b) / 2, 4)
error = c
row_0 = [a, b, c, f(a), f(c), f(a) * f(c) > 0, '-']

print(chart)
print(row_0)

if f(a) * f(c) < 0:
    b = c
else:
    a = c

c_prev = c

while programmed_error < error:
    c = round((a + b) / 2, 4)
    error = round(abs(c - c_prev), 4)
    c_prev = c
    rows = [a, b, c, f(a), f(c), f(a) * f(c) > 0, error]
    print(rows)
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
