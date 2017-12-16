list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

print(list_1 == list_2)
print(list_1 is list_2)

list_3 = list_2
print(list_2 == list_3)
print(list_2 is list_3)

print(list_2, list_3)
list_3[2] = 0
print(list_2, list_3)

import sys
print(list_1, sys.getrefcount(list_1))
print(list_2, sys.getrefcount(list_2))
print(list_3, sys.getrefcount(list_3))

print(type(list_1), type(list_2), type(list_3))

print(isinstance(True, int))
print(isinstance(True, float))
print(isinstance(True, object))

print(id(list_1), id(list_2), id(list_3))

print(str(list_1), repr(list_1))

a = repr('alphabet')
print(a)
b = eval(a)
print(b)
