def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    assert len(h) == len(w), "the length of two list must be equal"
    for x, y in zip(h, w):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ("Both list must contain only integers or floats.")
    return [w / (h ** 2) for h, w in zip(h, w)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    for x in bmi:
        if not isinstance(x, (int, float)):
            raise ("List must contain only integers or floats.")
    if not isinstance(limit, int):
        raise ("'limit' must be a integer")
    return [x > limit for x in bmi]
