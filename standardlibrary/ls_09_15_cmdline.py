import sys

if len(sys.argv) == 1:
    print("Usage: Python3 ls_09_15_cmdline.py <password>")
else:
    password = sys.argv[1]
    print("Password: ", password)
