#!/home/utils/Python-2.7.2/bin/python

import os
import re

sync1 = -1
print dir(sync1)
print id(sync1)
print type(eval(str(sync1)))
print type(eval(repr(sync1)))
print eval(str(sync1))
print eval(repr(sync1))
print type('Hello World!')
sync2 = sync1
print id(sync2)
sync1 += 1
print id(sync1)
print id(sync2)

foostr = 'abcde'
print foostr[::1]
print foostr[::2]
print foostr[::-1]
print foostr[::-2]

test = "new_test"
exp = "$teststring"
r = re.compile("\$(\w+)")
new_exp = r.sub(eval(r'1'), exp)
print new_exp

exit()
