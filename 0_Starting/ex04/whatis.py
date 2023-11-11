import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        sys.exit(0)

    try:
        num = int(sys.argv[1])
        if not isinstance(num, int):
            raise ValueError

        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")
