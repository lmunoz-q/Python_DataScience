import sys
from ft_filter import ft_filter


def is_ok(text, number):
    return len(text) > number


def main():
    assert len(sys.argv) == 3, "the arguments are bad"
    try:
        int(sys.argv[2])
    except:
        print("the arguments are bad")
    number = int(sys.argv[2])
    liste = sys.argv[1].split()

    print(ft_filter(lambda word: is_ok(word, number), liste))


if __name__ == "__main__":
    main()
