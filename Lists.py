# Modify lists
lst0 = [1, 2, 3]
lst1 = list(range(1, 4))

print(lst0)
lst0[0] = 0
lst0[-1] = 10
print(lst0)

print(lst1)
lst1[1:-1] = list(range(10, 15, 2))
print(lst1)

print(lst1)
del lst1[2:4]
print(lst1)

print(lst0)
lst0.append(list(range(10, 15, 1)))
print(lst0)

print(lst1)
lst1.extend([1, 2, 3])
print(lst1)

print(lst0)
lst0.insert(1, 10)
print(lst0)


lst3 = []
print(lst3)
for x in range(10):
    lst3.insert(0, x)
print(lst3)

lst4 = []
print(str(id(lst4)) + ": " + str(lst4))
for x in range(10):
    lst4.append(x)
print(lst4)
lst4.reverse()
print(str(id(lst4)) + ": " + str(lst4))
list.reverse(lst4)
print(str(id(lst4)) + ": " + str(lst4))
print(str(id(list(reversed(lst4)))))

print(lst0)
print(lst0.pop())
print(lst0)
print(lst0.pop(2))
print(lst0)

lst5 = list(range(10, 20, 1))
print(lst5)
lst5.remove(15)
print(lst5)

lst6 = ['a', 'b', 'c', 'A', 'B', 'C']
print(lst6)
lst6.sort(reverse=True)
print(lst6)

print(lst5)
print(lst6)
print(list(zip(lst5, lst6)))

for x, y in zip(lst5, lst6):
    print(x, y)

for i, v in enumerate(range(10, 51, 10), 1):
    print(i, v)

res = []
for x in range(1, 11):
    if x % 2 == 0:
        res.append(x*x)
print(res)

lst7 = [x * x for x in range(1, 11) if x % 2 == 0]
print(lst7)



