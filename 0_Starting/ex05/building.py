import sys

def count_char(string):
    """
    Count the number of characters in a string

    Args:
        string (str): string to count
    
    Returns:
        int: number of characters in the string
    """
    return len(string)

def count_upper(string):
    """
    Count the number of upper letters in a string
    
    Args:
        string (str): string to count
        
    Returns:
        int: number of upper letters in the string
    """
    return sum(1 for c in string if c.isupper())

def count_lower(string):
    """
    Count the number of lower letters in a string
    
    Args:
        string (str): string to count
        
    Returns:
        int: number of lower letters in the string
    """
    return sum(1 for c in string if c.islower())

def count_punctuation(string):
    """
    Count the number of punctuation marks in a string
    
    Args:
        string (str): string to count
        
    Returns:
        int: number of punctuation marks in the string
    """
    return sum(1 for c in string if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

def count_spaces(string):
    """
    Count the number of spaces in a string
    
    Args:
        string (str): string to count
        
    Returns:
        int: number of spaces in the string
    """
    return sum(1 for c in string if c == "\r" or c.isspace())

def count_digits(string):
    """
    Count the number of digits in a string
    
    Args:
        string (str): string to count
        
    Returns:
        int: number of digits in the string
    """
    return sum(1 for c in string if c.isdigit())

def print_building(string):
    """
    Print the number of characters, upper letters, lower letters, punctuation marks, spaces and digits in a string
    
    Args:
        string (str): string to count
        
    Returns:
        None
    """
    output = (
    f"The text contains {count_char(string)} characters:\n"
    f"{count_upper(string)} upper letters\n"
    f"{count_lower(string)} lower letters\n"
    f"{count_punctuation(string)} punctuation marks\n"
    f"{count_spaces(string)} spaces\n"
    f"{count_digits(string)} digits")
    print(output)


def main():
    if len(sys.argv) > 2:
        raise AssertionError("Too many arguments")
    elif len(sys.argv) == 1:
        user_input = input("What is the text to analyse?\n")
        print_building(user_input)
    else:
        print_building(sys.argv[1])

if __name__ == "__main__":
    main()
