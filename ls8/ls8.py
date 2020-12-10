#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

print(str(sys.argv))


cpu = CPU()


try:
    cpu.load(sys.argv[int(input(f'Enter a number 0-{len(sys.argv)-1}:  '))])
    cpu.run()
    
except IndexError:
    print("*** Please provide a directory and a filename --> ***")
