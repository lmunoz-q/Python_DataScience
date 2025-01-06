def slice_me(family: list, start: int, end: int) -> list:

    lines = len(family)
    cols = len(family[0])

    sFamily = family[start:end]

    sLines = len(sFamily)
    sCols = len(sFamily[0])
    print(f"My shape is : ({lines}, {cols})")
    print(f"My new shape is : ({sLines}, {sCols})")
    print("IL FAUT FAIRE GESTION DERREUR ")
    return sFamily
