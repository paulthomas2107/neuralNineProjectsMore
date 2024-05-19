from typing import NewType

a: int = 10

print(a)


ZipCode = NewType('ZipCode', int)


def printZip(code: ZipCode):
    print(code)


printZip(ZipCode(1234))  