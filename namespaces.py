a = 10

def fun():
    a = 100
    print(a)

print(a)
fun()
print(a)


b = 10
def fun_2():
    global b
    b = 100
    print(b)

print(b)
fun_2()
print(b)
print(b)


print(globals())
print(locals())

import sys
print(sorted(vars(sys).keys()) == sorted(dir(sys)))

def outer():
    a = 10
    print(a)
    def inner():
        nonlocal a
        a = 20
        print(a)
    inner()
outer()
print(a)

if __name__ == '__main__':
    print(True)
else:
    print(False)