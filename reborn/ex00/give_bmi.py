import sys

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    assert len(height) == len(weight), "the length of two list must be equal"
    for x, y in zip(height, weight):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raiseTypeError("Both list must contain only integers or floats.`")
    return [w / (h ** 2) for h, w in zip(height, weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [x > limit for x in bmi]
