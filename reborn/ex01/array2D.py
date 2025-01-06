def slice_me(family: list, start: int, end: int) -> list:
    lines = len(family)
    cols = len(family[0])
    for i in family:
        if not isinstance(i, list):
            raise AssertionError("'family' must be a array2D")
        for x in i:
            if not isinstance(x, (int | float)):
                raise AssertionError("array2D must contain integers or floats")
        if cols != len(i):
            raise AssertionError("List must contain lines with columns equal")

    sFamily = family[start:end]
    sLines = len(sFamily)
    sCols = len(sFamily[0])
    print(f"My shape is : ({lines}, {cols})")
    print(f"My new shape is : ({sLines}, {sCols})")
    return sFamily
