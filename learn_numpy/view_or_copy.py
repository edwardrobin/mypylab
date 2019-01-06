#!/usr/bin/env python

import numpy as np

a = np.arange(1,10)
print(a)
print(a.shape)
a.shape = (9,-1)
print(a.flags.owndata, a.base)
print(a)
print("1=" * 80)

# slicing : produce VIEW of array
a = np.arange(1,10)
b = a[:]
print(b.flags.owndata, b.base)
b[4] = 10
print(a)
print("2=" * 80)

# ravel : VIEW
a = np.arange(1,10).reshape(3,3)
b = a.ravel()
print(b.flags.owndata, b.base)
b[4] = 10
print(a)
print(b)
print("3=" * 80)

# reshape : VIEW
a = np.arange(1,10)
b = a.reshape((3,3))
print(b.flags.owndata, b.base)
a[4] = 10
print(b)
b[1,1] = 11
print(a)
print("4=" * 80)

# T (Transpose) : VIEW
a = np.arange(1,10)
aT = a.T
print(aT.flags.owndata, aT.base)
aTp = a.transpose()
print(aTp.flags.owndata, aTp.base)
aT[4] = 10
print(a)
print("5=" * 80)

# flatten : COPY
a = np.arange(1,10)
b = a.flatten()
print(b.flags.owndata, b.base)
b[4] = 10
print(a)
print("6=" * 80)

# vstack : COPY
a = np.arange(1,10).reshape(3,3)
b = np.arange(11,20).reshape(3,3)
c = np.vstack((a,b))
print(c.flags.owndata, c.base)
a[1,1] = 10
b[1,1] = 20
print(a)
print(b)
print(c)
print("7=" * 80)

print("Force a copy so that diminish the confusion caused by whether it's a view or not!")
aT = np.array(a.T, copy=True)
print(aT.flags.owndata, aT.base)
print("8=" * 80)
