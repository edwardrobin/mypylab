import c

v = c.functest
c.cv[0] += 1
print ("a import c.f : v id ->" + str(id(v)))
print ("a import cv : cv ->" + str(c.cv))