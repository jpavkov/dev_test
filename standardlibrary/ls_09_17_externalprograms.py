import subprocess

# process is an instance of another program

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

#
# completed = subprocess.run(["ls", "-l"])
# print("args", completed.args)
# print("returncode", completed.returncode)
# print("stderr", completed.stderr)
# print("stderr", completed.stdout)

# completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# print("args", completed.args)
# print("returncode", completed.returncode)
# print("stderr", completed.stderr)
# print("stderr", completed.stdout)

# completed = subprocess.run(["python", "standardlibrary/other.py"],
#                            capture_output=True, text=True)
# print("args", completed.args)
# print("returncode", completed.returncode)
# print("stderr", completed.stderr)
# print("stdout", completed.stdout)

try:
    completed = subprocess.run(["false"],
                               capture_output=True, text=True,
                               check=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
