import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def print_morse(string):
    """
    Print a string in morse code

    Args:
        string (str): string to print

    Returns:
        None
    """
    string = string.upper()
    string = [NESTED_MORSE[c] for c in string]
    string = "".join(string)
    string = string[:-1]
    print(string)


def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    elif [c for c in sys.argv[1].upper() if c not in NESTED_MORSE]:
        raise AssertionError("the arguments are bad")
    print_morse(sys.argv[1])


if __name__ == "__main__":
    main()
