#! /usr/bin/env python

# Initial version is from https://trstringer.com/python-shell-commands/

# If you just want to run a single binary and have no need for shell syntax or
# features:

import subprocess
import sys

cp = subprocess.run(
    ["echo", "hello world"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    # Or if you want to keep stdout/stderr separate then remove those params
    # and add:
    # capture_output=True
)

cmd_output = cp.stdout.decode()
print(cmd_output, end="")

if cp.returncode != 0:
    print(f"Error! {cp.returncode}")
    # Maybe exit if you shouldn't continue on failure
    sys.exit(cp.returncode)
