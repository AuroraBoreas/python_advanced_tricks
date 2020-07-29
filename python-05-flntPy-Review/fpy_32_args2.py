### approaches to define functions like C/C++, C#, VB.NET
# exmple 01
import sys
def is64bit() -> bool:
    return sys.maxsize > 2**32

# assert is64bit() == False, "you failed fool"


# example 02
def sayhello(name:str, times: int) -> None:
    fmt = "hello {}\n".format(name)
    print(fmt * times)
print(sayhello('ZL', 3))

# example 03
def calc(n: int) -> float:
    return n / 10
print(calc(11))