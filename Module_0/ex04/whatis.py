import sys

args = sys.argv

if len(args) < 2:
    exit(1)

if len(args) > 2:
    print("AssertionError: more than one argument is provided")
    exit(1)

try:
    arg = int(args[1])
except ValueError:
    arg = None
if arg is None:
    print("AssertionError: argument is not an integer")
    exit(1)

print("I'm Even.") if arg % 2 == 0 else print("I'm Odd.")
