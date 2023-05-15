#! /usr/bin/env python

# $ cat input.txt
# One, Two.
# OnE, Two.
# ONE, TWO.
# $ cat input.txt | python all_upper_to_lower.py
# One, Two.
# OnE, Two.
# one, two.

import sys

data = sys.stdin.readlines()
for line in data:
    line = line.rstrip('\n')
    new_line = line.lower() if line.isupper() else line
    print(new_line)
