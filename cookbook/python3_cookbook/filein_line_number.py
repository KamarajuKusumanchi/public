#! /usr/bin/env python3

# Requirements:
# * Print the contents of a file.
# * Prepend each line with the filename and line number.

# If you save this script as filein_line_number.py and make it executable, you can do
#  $ ./filein_line_number.py

# Initial version is from
# Python Cookbook by David Beazley, Brian K Jones
# 3rd edition, published in 2013
# Chapter 13, pg 540

# See also:
# * https://github.com/seanmcsIRL/cheat_sheets/blob/master/langs/python/pythonbooks/cookbook3rd/chap13/passwd.py

import fileinput

# The original version uses /etc/passwd file. But this is not available in
# Windows. So I decided to use __file__ which works on both Windows and Linux.
with fileinput.input(__file__) as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')
