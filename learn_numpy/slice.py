#!/usr/bin/env python

import numpy as np

a = np.arange(12).reshape(3,4)
print(str(a) + "__Print_1__\n")

i = np.array( [ [0,1],                        # indices for the first dim of a
                [1,2] ]  )
j = np.array( [ [2,1],                        # indices for the second dim
                [3,3] ]  )

print(str(a[i,j]) + "__Print_2__\n")

s = np.array( [i,j] )
print(str(a[list(s)]) + "__Print_3__\n")


print(str(a[i,2]) + "__Print_4__\n")

print(str(a[:,j]) + "__Print_5__\n")                     # i.e., a[ : , j  ]
