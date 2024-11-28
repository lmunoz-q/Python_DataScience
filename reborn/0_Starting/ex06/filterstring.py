import sys
from ft_filter import ft_filter


def is_ok(text, number):
    return len(text) > number


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")
        liste = sys.argv[1].split()

        print(ft_filter(lambda word: is_ok(word, number), liste))

    except AssertionError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
