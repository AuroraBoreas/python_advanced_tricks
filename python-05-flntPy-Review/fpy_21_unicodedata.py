# unicodedata is for standardization of Unicode string 
import unicodedata

# according to Unicode standard, é is canonical equivalent to 'e\u0301'. 
# But Python sees they are different.
print("without any standard")
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)

# so, we must normalize them in a way.
modes = [
    'NFC',
    'NFD',
    'NFKC', # ! be careful to use it. only use it in special cases like searching and indexing. not for permanent storing. it leads to data loss
    'NFKD', # ! be careful to use it. only use it in special cases like searching and indexing. not for permanent storing. it leads to data loss
]
print("using unicodedata.normalize() function to standardize our strings")
for mode in modes:
    print(len(unicodedata.normalize(mode, s1)), len(unicodedata.normalize(mode, s2)))
    print(unicodedata.normalize(mode, s1) == unicodedata.normalize(mode, s2))