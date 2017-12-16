# Data types and collections.
import sys
import decimal

# Integer numbers.
print(type(10))
print(sys.int_info)

# Floating-point numbers.
print((type(10.0)))
print(sys.float_info)

print(1e18+1e-6)

big = decimal.Decimal('1e18')
small = decimal.Decimal('1e-6')
print(big + small)

# Complex numbers.
c = 12 + 56j + 56 + 12j
print(c)

# Boolean values.
print(bool(0))
print(bool(''))
print(bool([]))

# Strings.
s = 'abcdefgh'
for c in s:
    print(c)

# Tuple
t = (1, "hello", 1.5)
for e in t:
    print(e)

# List
lst = [1, 2, 3]
print(lst)

# Dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(d['a'])

# Set
print({1, 2, 3, 5, 4, 3, 6, 2, 0, 1})