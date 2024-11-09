import sys

def count_upper(text: str) -> int:
    return sum(1 for c in text if c.isupper())

def count_lower(text: str) -> int:
    return sum(1 for c in text if c.islower())

def main():
    assert len(sys.argv) < 3, "more than one argument provied"
    if len(sys.argv) == 1:
        print("What is the text to count ?")
    else:
        print(f"The text contains {len(sys.argv[1])} characters:")
        print(f"{count_upper(sys.argv[1])} upper letters")
        print(f"{count_lower(sys.argv[1])} lower letters")

if __name__ == "__main__":
    main()
