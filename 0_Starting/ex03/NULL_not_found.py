def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} <class 'NoneType'>")
        return 0
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: {obj} <class 'float'>")
        return 0
    elif obj is False:
        print(f"Fake: {obj} <class 'bool'>")
        return 0
    elif isinstance(obj, str) and obj == "":
        print(f"Empty: {obj} <class 'str'>")
        return 0
    elif obj == 0:
        print(f"Zero: {obj} <class 'int'>")
        return 0
    else:
        print("Type not Found")
        return 0
    return 1
