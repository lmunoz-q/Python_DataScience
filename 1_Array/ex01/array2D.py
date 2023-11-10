def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise ValueError("Invalid input list")
    elif not isinstance(start, int) and not isinstance(end, int):
        raise ValueError("start and end must be a integer")
    elif len(family) > 2:
        l = len(family[0])
        for i in family:
            if l != len(i):
                raise ValueError("List are not the same size")
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(family[start:end])}, {len(family[start:end][0])})")
    return family[start:end]

