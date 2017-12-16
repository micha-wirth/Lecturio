g = (x * x for x in range(1, 11, 1))
print(g)

for x in g:
    print(x)

for x in g:
    print(x)


def simple_gen():
    print("Start 1")
    yield 1
    print("Start 2")
    yield 2
    print("Start 3")
    yield 3
    print("End")


s = simple_gen()
print(next(s))
print(next(s))
print(next(s))
# print(next(s))


def state(start=0):
    value = start
    yield value
    value += 1
    yield value
    value += 1
    yield value


st = state()
print(next(st))
print(next(st))
print(next(st))
# print(next(st))


def even_numbers(n):
    for x in range(n):
        if x % 2 == 0:
            yield x


e = even_numbers(10)
print(e)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
# print(next(e))

r = reversed(list(range(10)))
print(r)
print(next(r))
print(next(r))