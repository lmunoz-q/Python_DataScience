import sys


def print_lista(string, integer):
    """
    Print a list of words from a string that are longer
    than a given integer using list comprehension

    Args:
        string (str): string to print
        integer (int): minimum length of words to print

    Returns:
        None
    """
    words = string.split()
    words = [word for word in words if len(word) > integer]
    print(words)


def print_list_lambda(string, integer):
    """
    Print a list of words from a string that are longer
    than a given integer using lambda

    Args:
        string (str): string to print
        integer (int): minimum length of words to print

    Returns:
    """
    words = string.split()
    words = list(filter(lambda x: len(x) > integer, words))
    print(words)


def main():
    test = sys.argv[2]
    if not test.isdigit():
        raise AssertionError("the arguments are bad")
    if len(sys.argv) != 3 or not isinstance(sys.argv[1], str):
        raise AssertionError("the arguments are bad")
    print_lista(sys.argv[1], int(sys.argv[2]))
#    print_list_lambda(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()
