#!/usr/bin/python3
import sys
import os

print(os.path.basename(sys.argv[0]))
for arg in sys.argv[1:]:
    print(arg)