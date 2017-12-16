try:
    1 / 0
except ZeroDivisionError as error:
    print("Division durch Null")
    print(error)

try:
    1 / 0
except ZeroDivisionError as error:
    print(isinstance(error, ArithmeticError))

d = dict()
try:
    d['a']
except KeyError as error:
    print(error)

try:
    1 / 0
except ZeroDivisionError as error:
    # raise error

#raise ZeroDivisionError('Eigene Ausnahme geworfen')

def fun():
    print("Test")
    pass
    try:
        1 / 0
    except ZeroDivisionError as error:
        print("Division durch Null")
   # finally:
    #    print("Wird immer ausgeführt")


#fun()

class MyException(Exception):
    pass

raise MyException("Selbst geworfen")


d = {'a': 1, 'b': 2}
d.get('x', 24)

def my_get(d, k, default=None):
    try:
        return d[k]
    except KeyError:
        return default

my_get(d, 'x', 999)

