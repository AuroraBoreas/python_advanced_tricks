### This is my way to memorize scope types in Python. 
# LGEB
# local: locals(), nonlocal
# global: globals()
# enclosure: vars()
# built-ins

b = 9
def f2(a: int) -> None:
    print(a)
    print(b)
    # b = 6 # commment out to see an interesting behavor in Python

if __name__ == "__main__":
    import dis
    dis.dis(f2)
    # disassemble f2() while commenting line 12
    # CPython VM operations
    """
    10          0 LOAD_GLOBAL              0 (print)
                2 LOAD_FAST                0 (a)
                4 CALL_FUNCTION            1
                6 POP_TOP

    11           8 LOAD_GLOBAL              0 (print)
                10 LOAD_GLOBAL              1 (b)
                12 CALL_FUNCTION            1
                14 POP_TOP
                16 LOAD_CONST               0 (None)
                18 RETURN_VALUE
    """
    # disassemble f2() without commenting line 12
    # CPython VM operations
    """
    10          0 LOAD_GLOBAL              0 (print)
                2 LOAD_FAST                0 (a)
                4 CALL_FUNCTION            1    
                6 POP_TOP

    11           8 LOAD_GLOBAL              0 (print)
                10 LOAD_FAST                1 (b)
                12 CALL_FUNCTION            1
                14 POP_TOP

    12          16 LOAD_CONST               1 (6)
                18 STORE_FAST               1 (b)
                20 LOAD_CONST               0 (None)
                22 RETURN_VALUE
    """