# Newton-Raphson method

import math
import numpy as np
import sympy as sp
from sympy import *

x = Symbol('x')

def f(x):
    return (math.e ** (- x)) - x

def f_prime(x):
    return ((math.e ** (- x)) - x).diff(x)


print(f(2))
print(f_prime(x))

xi = float(input('Insert starting point: '))
programmed_error = float(input('Insert programmed error: '))

