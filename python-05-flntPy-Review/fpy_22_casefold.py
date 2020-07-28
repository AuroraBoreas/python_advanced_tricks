# What?
# ? what is casefold()?
# ! it means to alter all test into lowercase.
# str.casefold()
# ? but what is the difference between str.casefold() and str.lower()?

s = "Hello World!"
print(s.casefold())
print(s.lower())

# it means no difference? if so, why str.casefold() is introduced after str.lower()? it violates DRY
assert s.casefold() == s.lower()

"""str.lower()
Return a copy of the string with all the cased characters [4] converted to lowercase.
The lowercasing algorithm used is described in section 3.13 of the Unicode Standard
"""

"""str.casefold()
Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. 
For example, the German lowercase letter 'ß' is equivalent to "ss". 
Since it is already lowercase, lower() would do nothing to 'ß'; casefold()converts it to "ss".

The casefolding algorithm is described in section 3.13 of the Unicode Standard
"""

"""
Python >= 3.4, str.casefold() returns 116 more different codepoints than str.lower()
"""

eszett = 'お'
import unicodedata
print(unicodedata.name(eszett))
print(eszett.casefold()) # did nothing