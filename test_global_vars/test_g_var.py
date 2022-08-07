#!/usr/bin/env python3

import a
import b

from a import print_global_var as a_print
from b import print_global_var as b_print

a_print()
b_print()

print("\n======================\n")

print(a.__name__)
print(a.__file__)
print(a.__package__)

print("\n======================\n")

print(a_print.__globals__["g_var"])
print(b_print.__globals__["g_var"])


