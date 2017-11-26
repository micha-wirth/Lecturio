d0 = {'a': 1, 'b': 2, 'c': 3}
print(d0)

# Pairs of elements.
print(len(d0))

# Returns value of corresponding key.
print(d0['a'])

# Assign value of corresponding key.
d0['a'] = 0
print(d0)

d0['x'] = 100
print(d0)

# Return all keys of dictionary.
print(d0.keys())

# Return all values of dictionary.
print(d0.values())

# Return all key-value-pairs as tuple.
print(d0.items())

# Update dictionary.
d0.update({'a': 100, 'y': 5})
print(d0)

# Generate new dictionary with fromkeys.
d1 = dict.fromkeys('abc', [])
print(d1)

# Generate new dictionary with dict.
d2 = dict()
d3 = dict({('a', 1), ('b', 2)})
d4 = dict(zip('abc', [1, 2, 3]))
print(d2)
print(d3)
print(d4)

d1['c'].append(100)
print(d1)

d1['c'] = [200]
print(d1)

# Get method
print(d0.get('a', -1))
print(d0.get('z', None))
print(d0.get('y') is None)



