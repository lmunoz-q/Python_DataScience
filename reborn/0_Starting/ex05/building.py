import sys


def count_upper(text: str) -> int:
    """count_upper(tecount_upper(text: str) -> itr) -> i
    Count the number of upper letters in a string

    Args:
        text (str): string to count

    Returns:
        int: number of upper letters in the string
    """
    return sum(1 for c in text if c.isupper())


def count_lower(text: str) -> int:
    """
    Count the number of lower cases in a string

    Args:
        text (str): string to count

    Returns:
        int: number of lower letters in the string
    """
    return sum(1 for c in text if c.islower())


def count_number(text: str) -> int:
    """
    Count the number of digits in a string

    Args:
        text (str): string to count

    Returns:
        int: number of digits in the string
    """
    return sum(1 for c in text if c.isdigit())


def count_spaces(text: str) -> int:
    """
    Count the number of differents spaces in a string

    Args:
        text (str): string to count

    Returns:
        int: number of differents spaces in the string
    """
    return sum(1 for c in text if c.isspace())


def count_mark(text: str) -> int:
    """
    Count the number of punctuation marks in a string

    Args:
        text (str): string to count

    Returns:
        int: number of punctiation marks in the string
    """
    return sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")


def print_building(text: str):
    print(f"The text contains {len(text)} characters:")
    print(f"{count_upper(text)} upper letters")
    print(f"{count_lower(text)} lower letters")
    print(f"{count_mark(text)} punctuation marks")
    print(f"{count_spaces(text)} spaces")
    print(f"{count_number(text)} digits")


def main():
    assert len(sys.argv) < 3, "more than one argument provied"
    if len(sys.argv) == 1:
        text = input("What is the text to count ?\n")
        print_building(text)
    else:
        print_building(sys.argv[1])


if __name__ == "__main__":
    main()
