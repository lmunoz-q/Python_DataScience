import sys

assert len(sys.argv) < 3, "more than one argument is provided"

if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if number % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd.")
