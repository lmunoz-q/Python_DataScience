def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    Calculate a list of Body Mass Index (BMI) values
    based on given heights and weights.

    Parameters
    ----------

    h (height) : int | float
        List of heights in meters.

    w (weight) : int | float
        List of weights in kilograms.

    Returns
    -------
    list[int | float]
        List of BMI, computed using the formula:
        BMI = weight / (height ** 2)

    Raises
    ------
    AssertionError
        If the two input lists do not have the same length.

    TypeError
        If any element in the lists is not an int or a float.
    """
    assert len(h) == len(w), "the length of two list must be equal"
    for x, y in zip(h, w):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both list must contain only integers or floats.")
    return [w / (h ** 2) for h, w in zip(h, w)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare each BMI value to a limit and return a list of boolean values.

    Parameters
    ----------

    bmi : list[int | float]
        List of BMI values to check.

    limit : int
        Threshold to compare each BMI value against.

    Returns
    -------

    list[bool]
        List indicating whether each BMI is greater than the limit.

    Raises
    ------

    TypeError
        if BMI values are not numbers or if the limit is not an integer.
    """
    for x in bmi:
        if not isinstance(x, (int, float)):
            raise TypeError("List must contain only integers or floats.")
    if not isinstance(limit, int):
        raise TypeError("'limit' must be a integer")
    return [x > limit for x in bmi]
