#!/usr/bin/env python3

import readchar
from colorama import Fore, Style
def printAllCharsUpTo (stop_char):

    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))
        print('teste')


def readAllUpTo (stop_char):


    counted_numeric_key = 0
    counted_non_numeric_key=0

    while True :
        print('type something (to stop:press "X") ')
        key = readchar.readkey()
        if str.isnumeric(key):
            counted_numeric_key += 1
        else:
            counted_non_numeric_key += 1
        print('Thank you for typing key ' +
              Fore.GREEN + (key) + Style.RESET_ALL)
        if key == 'X':
            print('You broke the cicle Zé')
            break
    print(Fore.BLUE+'You entered ' + str(counted_numeric_key) +
          ' numbers.'+Style.RESET_ALL)
    print(Fore.RED+'You entered ' + str(counted_non_numeric_key)
          + ' others.'+Style.RESET_ALL)
def main():

    # Ex4 b)
    print('Aí estão os chars')
    readAllUpTo('X')

    # Ex4 a)
    #  print('Aí está o char')
    #  key = readchar.readchar()
    #  printAllCharsUpTo(key)


if __name__ == '__main__':
    main()
