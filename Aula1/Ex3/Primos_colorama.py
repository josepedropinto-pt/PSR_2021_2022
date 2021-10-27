#!/usr/bin/env python3
# inicio=int(input('Inicio do intervalo: '))
# fim=int(input('fim do intervalo: '))
#
# for no in range(inicio, fim+1):
#
#     for div in range(2, 9):
#             if (no % div) == 0:
#              break
#             print('O número' + str(no) + 'não é primo!')
#     else:
#         print('O número' + str(no) + 'é primo')
#
from colorama import Fore, Back, Style
maximum_number = 100
# inicio=int(input('Inicio do intervalo: '))
# fim=int(input('fim do intervalo: '))

def isPrime(value):
    print('\n Vamos confirmar se o' + " " + str(value) + " " +'é primo...')

    for div in range(2, value):
        resto = value % div
        print(Fore.BLUE + 'Dividindo o valor'+ " " + str(value) + " " + 'pelo divisor'+ " " + str(div) + " " + 'Dá resto' + " " + str(resto))
        if resto == 0:
            return False
    return True
    # return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))
    count=0
    for i in range(0, maximum_number):
        if isPrime(i):
            count=count+1
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')
        print('Existem entre' + " " + str(1) + " " + 'e' + " " + str(maximum_number) + " " + 'cerca de'+ " " + str(count) + " " + 'números primos!!' )
if __name__ == "__main__":
    main()

#  | grep "string to find" | wc -l
# finding string and counting the number of lines
