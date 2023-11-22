def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Input lists must have the same size")

    ret_list = []
    for i, y in zip(height, weight):
        if not (isinstance(i, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Height and weight must be integers or floats")
        ret_list.append(y / i ** 2)
    return ret_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(i, (int, float)) for i in bmi):
        raise ValueError("Invalid BMI values in the input list")

    ret_list = []
    for i in bmi:
        ret_list.append(i > limit)
    return ret_list
