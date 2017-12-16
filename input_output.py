#
# in_string = input("Bitte etwas eingeben! ")
# print(in_string)

in_string = ("Bitte eine Zahl eingeben! ")
print(str(in_string))


# Command line arguments
import sys

print(sys.argv)

# Read and write files.
fobj = open('data.txt', 'w')
if fobj.writable():
    fobj.write('Line 1\nLine 2\n\n')
fobj.close()

fobj = open('data.txt', 'r')
print(fobj.readlines())
print(fobj.flush())
fobj.close()

print(fobj)

fobj = open('data.txt')
if fobj.readable():
    print(fobj.read())
else:
    print("Datei nicht lesbar!")

print(fobj.tell())
print(fobj.read())
print(fobj.seek(0))
print(fobj.read())

fobj.seek(0)
print(fobj.tell(), fobj.readline())
print(fobj.tell(), fobj.readline())

# File objects are iteratable.
fobj.seek(0)
for line in fobj:
    print(line, end='')

fobj.close()

with open('data.txt') as fobj:
    for line in fobj:
        print(line, end='')
    print(fobj.closed)
print(fobj.closed)

print(dir(fobj))

# Pickle module
import pickle

data = pickle.dumps([100, 200, 300])
print(data)
data = pickle.loads(data)
print(data)


fobj = open('data.pickle', 'wb')
pickle.dump(data, fobj)
fobj.close()

fobj = open('data.pickle', 'rb')
print(fobj.read())
pickle.load(fobj)
fobj.close()