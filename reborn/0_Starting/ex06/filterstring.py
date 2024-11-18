import sys

def ft_filter(function, iterable):
    return [x for x in iterable if function(x)]

def is_ok(text, number):
    if len(text) > number:
        return True
    else:
        return False

def main():
    assert len(sys.argv) == 3, "the arguments are bad"
    liste = sys.argv[1].split()
    chaine = sys.argv[1]

    print(f"{liste}")
    print(f"{chaine}")
    print(f"{len(liste)}")
    print(f"{len(chaine)}")

    print(ft_filter(is_ok(chaine, 4), liste))

if __name__ == "__main__":
    main()
