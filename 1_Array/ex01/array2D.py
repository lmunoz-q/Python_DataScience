def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array (list of lists) from row index `start` to `end`
    and display the original and new shape.

    Parameters
    ----------

    family : list of list of int or float
        2D array to slice. Each sublist must be of the same length
        and contain numbers.

    start : int
        Starting index for slicing (inclusive).

    end : int
        Ending index for slicing (exclusive).

    Returns
    -------

    list
        Sliced 2D array (same number of columns, but fewer rows).

    Raises
    ------

    TypeError
        If family is not a 2D list of int or float.
    ValueError
        If rows don't all have the same number of columns.
    IndexError
        If trying to access columns in an empty list.
    """
    if not family:
        raise ValueError("'family' must not be empty")
    lines = len(family)
    cols = len(family[0])
    for i in family:
        if not isinstance(i, list):
            raise TypeError("'family' must be a list of lists")
        for x in i:
            if not isinstance(x, (int, float)):
                raise TypeError("Elements must be integers or floats")
        if cols != len(i):
            raise ValueError("All rows must have the same number of columns")

    sFamily = family[start:end]
    sLines = len(sFamily)
    sCols = len(sFamily[0])
    print(f"My shape is : ({lines}, {cols})")
    print(f"My new shape is : ({sLines}, {sCols})")
    return sFamily
