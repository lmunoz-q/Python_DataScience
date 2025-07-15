def square(x : int | float) -> int | float:
    return x * x

def powww(x : int | float) -> int | float:
    ret = x
    for i in range(x - 1):
        ret *= x
    return ret

def outer(x : int | float, function) -> objects:
        count = 0
    def inner() -> float:
