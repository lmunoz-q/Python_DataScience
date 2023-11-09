def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    ret_list = []
    for i, y in zip(height, weight):
        ret_list.append(y / i ** 2)
    return ret_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ret_list = []
    for i in bmi:
        ret_list.append(i > limit)
    return ret_list
