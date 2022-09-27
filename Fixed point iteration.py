# Fixed point iteration

import math
import numpy as np

def f(x):
    return (math.e ** (- x)) - x

def g(x):
    return math.e ** - x

a = round(float(input('Insert a: ')), 4)
b = round(float(input('Insert b: ')), 4)
programmed_error = float(input('Insert programmed error: '))