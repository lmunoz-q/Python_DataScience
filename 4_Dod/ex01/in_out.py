def square(x: int | float) -> int | float:
    """
    Compute the square of the given number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Compute the exponentiation of x by itself (x ** x).
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return a closure function that applies the given function iteratively
    to a stored value starting from x.

    Each call to the returned function applies the function to the current
    value and updates it.
    """
    value = x

    def inner() -> float:
        nonlocal value
        value = function(value)
        return value

    return inner
