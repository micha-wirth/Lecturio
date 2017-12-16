s1 = 'String mit Hochkommas'
print(s1)

s2 = "String mit Anführungszeichen"
print(s2)

print(s1.upper())
print(s1.lower())
print(s1.center(10, '!'))

s = 'String'
print(s.encode('utf-8'))
print(s.encode('latin-1'))

my_string = 'String'
my_list = list(my_string)
print(my_string)
print(my_list)
print(str().join(my_list))

print(my_string.ljust(10, '#'))
print(my_string.rjust(10, '#'))

print(' #String# '.lstrip())
print(' #String# '.rstrip())
print(' #String# '.strip())

print('S t r i n g'.split())
