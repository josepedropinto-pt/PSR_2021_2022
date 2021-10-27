#!/usr/bin/env python3

import readchar
from colorama import Fore, Style
def printAllCharsUpTo (stop_char):

    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))
        print('teste')


def readAllUpTo (stop_char):


    #Criar a lista e colocar lá material

    keys = [] #começar com lista vazia

    while True :
        print('type something (to stop:press "X") ')
        key = readchar.readkey()
        if key == 'X':
            print('You broke the cicle Zé')
            break
        else:
            keys.append(key) #append adiciona elemento fim do array
    print('The keys that you pressed are ' + str(keys))



    #Analisar a lista e contar
    counted_numeric_key = 0
    counted_non_numeric_key = 0
    lista_numeros = []
    lista_outros = []

    for i in keys:

        if str.isnumeric(i):
            counted_numeric_key += 1
            lista_numeros.append(i)
            #Exercicio 5 d)
            lista_numeros= sorted(lista_numeros, reverse=False)

        else:
            counted_non_numeric_key += 1
            lista_outros.append(i)
            lista_outros= sorted(lista_outros, reverse=False)

    print(Fore.LIGHTMAGENTA_EX + 'This are the numerics '
                                 'that you pressed '
          + str(lista_numeros) + Style.RESET_ALL )

    print(Fore.YELLOW + 'This are the non numerics '
                                 'that you pressed '
          + str(lista_outros) + Style.RESET_ALL)

    print(Fore.BLUE+'You entered ' + str(counted_numeric_key) +
          ' numbers.'+Style.RESET_ALL)
    print(Fore.RED+'You entered ' + str(counted_non_numeric_key)
          + ' others.'+Style.RESET_ALL)

#5 c)

    dic_others = {}

    for no, i in enumerate(keys):
        if not str.isnumeric(i):
            dic_others[no] = i

    print(Fore.LIGHTBLACK_EX + 'dic_others ' + str(dic_others))


def main():
    print('Aí estão os chars')
    readAllUpTo('X')


if __name__ == '__main__':
    main()
