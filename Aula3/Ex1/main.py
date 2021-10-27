#!/usr/bin/env python3

from colorama import Fore, Style,Back
from time import time, ctime
import math
date = ctime()
print("Today is "+Fore.LIGHTMAGENTA_EX + date + Style.RESET_ALL)

init_time = time()

for i in range(0, 500000):
    math.sqrt(i)

end_time = time()

ellapsed_time = end_time - init_time

print('Total ellapsed time of ' + Back.LIGHTCYAN_EX+str(ellapsed_time)+Style.RESET_ALL +
      " " + Fore.RED+ 'seconds'+Style.RESET_ALL)
