#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
print(sys.argv[0])

try:
    cpu.load('D:\CSpt12\Computer-Architecture\ls8\examples\print8.ls8')
    cpu.run()
    
except IndexError:
    print("*** Please provide a directory and a filename --> ***")
