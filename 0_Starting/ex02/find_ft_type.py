# This function will find the type of the object passed as parameter and print it.
def all_thing_is_obj(obj: any) -> int:
    if isinstance(obj, list):
        print("List:", type(obj))
    elif isinstance(obj, tuple):
        print("Tuple:", type(obj))
    elif isinstance(obj, set):
        print("Set:", type(obj))
    elif isinstance(obj, dict):
        print("Dict:", type(obj))
    elif isinstance(obj, str):
        if obj == "Brian":
            print(obj, "is in the kitchen:", type(obj))
        else:
            print("String:", type(obj))
    else:
        print("Type not found")
    return 42