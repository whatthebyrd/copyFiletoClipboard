#!/usr/bin/python3

# copyF2CB
# Invoke by: copyF2CB <Filename>
# Takes contents of file and places into clipboard. Uses pyperclip; see website for OS-specific installs: https://pypi.org/project/pyperclip/
# Original Creation: 26JUL20
# Released under Apache 2.0 License

import os
import sys
import pyperclip

if os.path.exists(sys.argv[1]):  # Check if path is valid
    file = open(sys.argv[1], "r")  # Open file in read-only mode
    file_cont = file.read()  # Place file contents into var
    file.close()  # Close file
    pyperclip.copy(file_cont)
    print("Successfully copied contents of " + str(sys.argv[1]) + ".")
else:
    print("Path invalid. Exiting.")