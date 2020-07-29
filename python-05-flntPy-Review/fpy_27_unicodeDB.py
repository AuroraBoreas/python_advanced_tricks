### unicodedata has functions to acquire meta data or info of characters.
# unicodedata.name()
# unicodedata.numeric()
import unicodedata
import re

re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
# you can utilize format() function like this... aw, well
print(format('hello world', '-^80'))
for char in sample:
    print('U+%04x' % ord(char),
        'u+{:04x}'.format(ord(char)),
        char.center(6),
        're_dig' if re_digit.match(char) else '-',
        'isdig' if char.isdigit() else '-',
        'isnum' if char.isnumeric() else '-',
        format(unicodedata.numeric(char), '5.2f'),
        unicodedata.name(char),
        sep='\t'    
    )