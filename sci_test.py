#!/usr/bin/env python3

import sys
print(sys.version)

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print(a, b, c, end="\n")

#import jedi
#jedi.set_debug_function()
#jedi.Script('import math; math.').completions()
#jedi.Script('import numpy; numpy.').completions()
#jedi.Script('import sympy; sympy.').completions()

import jedi
jedi.__version__
