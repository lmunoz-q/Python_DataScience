import sys

# Check the number of arguments
if len(sys.argv) != 2:
    raise AssertionError("more than one argument is provided")
# Try to parse the argument as an integer
try:
    arg = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument must be an integer")
# Check if the integer is even or odd
else:
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
