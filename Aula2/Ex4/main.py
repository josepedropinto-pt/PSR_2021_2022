#!/usr/bin/env python3

import readchar

def printAllCharsUpTo(stop_char):

    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))
        print('teste')

def main():
    print('Aí está o char')
    key = readchar.readchar()
    printAllCharsUpTo(key)


if __name__ == '__main__':
    main()

#comment to push from pycharm

#send back to pych