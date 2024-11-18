import sys

def ft_filter(function, iterable):
    return [x for x in iterable if function(x)]

def is_ok(text, number):
    if len(text) > number:
        return text

def main():
    assert len(sys.argv) == 3, "the arguments are bad"
    liste = sys.argv[1].split()
    chaine = sys.argv[1]

    print(f"{liste}")
    print(f"{chaine}")

if __name__ == "__main__":
    main()
