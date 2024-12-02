import sys
from ft_filter import ft_filter


def is_ok(text, number):
    """
    Return True if the len of the text is upper than the number given

    Args:
        text (str): string to analyze
        number (int): the len we want to

    Return:
        True or False
    """
    return len(text) > number


def print_list(text, integer):
    """
    Print a list of words from a string that are longer
    than a given integer using list comprehension

    Args:
        string (str): string to print
        integer (int): minimum length of words to print

    Returns:
        None
    """
    words = text.split()
    print([word for word in words if is_ok(word, integer)])


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")
        liste = sys.argv[1].split()
        # print_list(sys.argv[1], number)
        print(ft_filter(lambda word: is_ok(word, number), liste))

    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
