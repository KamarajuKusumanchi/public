#! /usr/bin/env python3

# Script to accept input via redirection, pipes or input files

# If you save this script as filein.py and make it executable, you can do all
# of the following and get the expected output:
#   $ ls | ./filein.py          # Prints a directory listing to stdout.
#   $ ./filein.py /etc/passwd   # Reads /etc/passwd to stdout.
#   $ ./filein.py < /etc/passwd # Reads /etc/passwd to stdout.

# Initial version is from
# Python Cookbook by David Beazley, Brian K Jones
# 3rd edition, published in 2013
# Chapter 13, pg 539-540

# See also:
# * https://github.com/seanmcsIRL/cheat_sheets/blob/master/langs/python/pythonbooks/cookbook3rd/chap13/filein.py

import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
