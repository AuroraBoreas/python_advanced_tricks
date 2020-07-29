### a fantastic example shows how * and ** works in a function.
# a basic html function to generate html tags
# just like tuple or list decomp, it works in function arguments too.
"""
    tag function has the following abilities.
    >>> tag('br')
    '<br />'
    >>> tag('p', 'hello')
    '<p>hello</p>'
    >>> tag('p', 'hello', 'world')
    '<p>hello</p>'
    '<p>world</p>'
    >>> tag('p', 'hello', id=33)
    '<p id="33">hello</p>'
    >>> tag('p', 'hello', 'world', cls='sidebar')
    '<p class="sidebar">hello</p>'
    '<p class="sidebar">world</p>'
    >>> tag(content="testing", name="img")
    '<img content="testing" />'
    >>> tag(**{'name':'img', 'title':'Sunset Boulevard', 'src':'sunset.jpg', 'cls':'framed'})
    '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
    >>> a, b = [1, 2]
    >>> a
    1
    >>> b
    2
    >>> a, b, *rest = (3, 4, 5, 6)
    >>> a
    3
    >>> b
    4
    >>> rest
    [5, 6]
    >>> a, _ = 3, 4, 
    >>> a
    3
"""

def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                    for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % 
                    (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

if __name__ == "__main__":
    # print(tag('br'))
    # print(tag('p', 'hello'))
    # print(tag('p', 'hello', 'world'))
    # print(tag('p', 'hello', id=33))
    # print(tag('p', 'hello', 'world', cls='sidebar'))
    # print(tag(content="testing", name="img"))
    # my_tags = dict(
    #                 name='img',
    #                 title='Sunset Boulevard',
    #                 src='sunset.jpg',
    #                 cls='framed',
    # )
    # print(tag(**my_tags))

    import doctest
    doctest.testmod()