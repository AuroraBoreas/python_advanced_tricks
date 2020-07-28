
# string -> bytes. difference between several encoding methods
def latin_encoding():
    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'E1 Niño'.encode(codec), sep='\t')
    return

# TODO: deals with UnicodeEncodeError
# what? UnicodeEncodeError occurs during string object -> bytes object. 
# it means encoding problem.
city = 'São Paulo'
print(city.encode('utf8'))
print(city.encode('utf16'))
print(city.encode('iso8859_1'))
# ! UnicodeEncodeError
# print(city.encode('cp437'))
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))

# TODO: deals with UnicodeDecodeError
octets = b'Montr\xe9al'
for decodec in ['cp1252', 'iso8859_7', 'koi8_r', 'utf8']:
    try:
        print(octets.decode(decodec))
    except UnicodeDecodeError:
        print(octets.decode(decodec, errors='replace'))

# ? How can I find out encoding of a bytes object?
# ! No, you can't. Someone tells you the encoding
# Chardet may help. It can 30 sorts of encoding.

# BOM (byte-order-mark) may also help. using 'UTF-16' to encode.
# using 'UTF-16LE'(explicit little-endian) or 'UTF-16BE'(explicit big-endian) to encode won't generate BOM
u16 = 'El Niño'.encode('utf16')
# TODO: find out the header of the bytes object. it's \xff\xfe
print(u16)
# TODO: word E is U+0045(69D)
print(list(u16))

# TODO: Pragmatic Unicode -- Unicode sandwich -- bytes -> str; 100% str; str -> byte
with open('cafe.txt', 'w', encoding='utf-8') as f:
    f.write('café')
# without specifying explicit encoding ...
# the best practice is to open a file with explicit encoding if possible
with open('cafe.txt', 'r') as f:
    print(f.read())
with open('cafe.txt', 'r', encoding='UTF8') as f:
    print(f.read())

# exploring encoding value
import sys, locale
expressions = """
locale.getpreferredencoding()
type(my_file)
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.stderr.isatty()
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
sys.stdout.isatty()
for expression in expressions.split(): # even source code is written like this. i don't like. because str.split() in a loop
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))