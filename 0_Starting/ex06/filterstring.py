import sys



def main():
    if len(sys.argv) > 3:
        raise AssertionError("Wrong arguments, needed 2")
    else:
        printme()

if __name__ == "__main__":
    main()

