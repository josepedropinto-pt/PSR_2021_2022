#!/usr/bin/env python3

no = int(input('Coloque o máximo de número a analisar: '))

maximum_number = no

from colorama import Fore, Style
from my_functions import isPerfect

def main():

    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print(Fore.GREEN + Style.BRIGHT+
            'Number ' + str(i) + ' is perfect.'+Style.RESET_ALL)

        else:
            print(Fore.RED + Style.BRIGHT +
                  'Ora bolas, o ' + str(i) + ' não é perfeito'
                  +Style.RESET_ALL)


if __name__ == "__main__":
    main()
