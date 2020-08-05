import re

text    = 'abbaaabbbbaaaaa'
pattern = 'ab'

def addBreaker(func):
    def inner(*args, **kwargs):
        Breaker = '\n{:-^50}'
        print(Breaker.format(''))
        func(*args, **kwargs)
    return inner

@addBreaker
def test_patterns(patterns, text):
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[s:e].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return

if __name__ == "__main__":
    test_patterns(patterns=[('ab', "'a' followed by 'b'")], text=text)