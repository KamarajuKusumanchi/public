#! /usr/bin/env bash
# Script to analyze and remove an obsolete package.
#
# To identify obsolete packages, you can use
# % apt list "?obsolete" 2>/dev/null | cut -f 1 -d '/' | popsort.py
set -ux
rmadison $1
aptitude why $1
sudo apt-get remove --purge $1
