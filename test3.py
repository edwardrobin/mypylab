#!/home/utils/Python-3.5.2/bin/python3

import os
import re


list1 = [1, 2, 3]
print (id(list1), list1)
list2 = [4, 5]
print (id(list2), list2)
list3 = list1 + list2
print (id(list3), list3)
list1 += list2
print (id(list1), list1)

exit()
