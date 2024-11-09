import sys

def count_upper(str text) -> int
    x = 0
    for i in text:
        if i.isupper():
            x += 1
    return x

def main():
    assert len(sys.argv) < 3, "more than one argument provied"
    if len(sys.argv) == 1:
        print("What is the text to count ?")
    else:
        print(f"The text contains {count_upper(sys.argv[1])} characters:")

if __name__ == "__main__":
    main()
