def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        if object == "Brian":
            print(f"Brian is in the kitchen : {type(object)}")
        else:
            print(f"Str : {type(object)}")
    elif isinstance(object, complex):
        print(f"Complex : {type(object)}")
    elif isinstance(object, range):
        print(f"Range : {type(object)}")
    elif isinstance(object, frozenset):
        print(f"Frozenset : {type(object)}")
    elif isinstance(object, bool):
        print(f"Bool : {type(object)}")
    elif isinstance(object, bytes):
        print(f"Bytes : {type(object)}")
    elif isinstance(object, bytearray):
        print(f"Bytearray : {type(object)}")
    elif isinstance(object, memoryview):
        print(f"Memoryview : {type(object)}")
    elif isinstance(object, int):
        if object == 10:
            print("Type not found")
        else:
            print(f"Int : {type(object)}")
    elif isinstance(object, float):
        print(f"Float : {type(object)}")
    else:
        print("Type not found")
    return 42
