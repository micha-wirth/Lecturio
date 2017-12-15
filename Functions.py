def fun():
    None


def add(a, b):
    return a + b


print(add(1, 7))
print(add(1.0, 7))
print(add('a', 'b'))


def show(text):
    print(text)
    # return None


def sub(a, b):
    return a - b


print(sub(2, 1))
# print(sub('a', 'b'))
print(sub(b=2, a=1))
# print(sub(a='a', b='b'))

print(range(3))
print(range(1, 3))
print(range(1, 10, 2))


def func(*args, **kwargs):
    print(args)
    print(kwargs)


print(func())
print(func(1))
print(func(1, 2, ('a', 10), dict(zip('abc', list((1, 2, 3))))))
print(func(list('abc')))


def larger(a, b):
    return a > b


print(larger(2, 1))
print(larger(2, 2))
