def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} <class 'NoneType'>")
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: {obj} <class 'float'>")
    elif obj is False:
        print(f"Fake: {obj} <class 'bool'>")
    elif isinstance(obj, str) and obj == "":
        print(f"Empty: {obj} <class 'str'>")
    elif obj == 0:
        print(f"Zero: {obj} <class 'int'>")
    else:
        print("Type not Found")
    return 1
