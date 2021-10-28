#!/usr/bin/env python3

from colorama import Fore, Style
from collections import namedtuple

No_complexos = namedtuple('No_complexos', ['real','imag'])

def addComplex(x, y):

    soma = No_complexos(x.real+y.real, x.imag+y.imag)
    return soma

def multiplyComplex(x, y):

    multi = No_complexos(x.real*y.real-x.imag-y.imag,
                         x.real*y.imag + x.imag*y.real)
    return multi


def printComplex(x):

    print((str(x.real) + '+' + str(x.imag) + 'i'))

def main():


    c1 = No_complexos(5, 3)
    c2 = No_complexos(-2, 7)

    c3 = addComplex(c1, c2)

    printComplex(c1)
    printComplex(c3)
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()
