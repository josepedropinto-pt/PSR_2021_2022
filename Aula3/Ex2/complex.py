#!/usr/bin/env python3

from colorama import Fore, Style

def addComplex(x, y):

    real1=x[0]
    imag1=x[1]
    real2=y[0]
    imag2=y[1]
    add_real=real1+real2
    add_imag=imag1+imag2
    return (add_real, add_imag)

def multiplyComplex(x, y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]

    result_real = a*c-b*d
    result_imag = a*d + b*c
    return (result_real, result_imag)


def printComplex(x):

    real=x[0]
    imag=x[1]
    print((str(real) + '+' + str(imag) + 'i'))

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)

    printComplex(c1)
    printComplex(c3)

    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()
