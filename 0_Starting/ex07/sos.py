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


def morsify(text):
    """
    Print a string in morse code

    Args:
        string (str): string to print

    Returns:
        None
    """
    ret = ""
    for i in text:
        ret += NESTED_MORSE[(i.upper())]
    ret = ret[:-1]
    print(ret)


def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    if [i for i in sys.argv[1].upper() if i not in NESTED_MORSE]:
        raise AssertionError("the arguments are bad")
    morsify(sys.argv[1])


if __name__ == "__main__":
    main()
