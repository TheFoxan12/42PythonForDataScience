
def NULL_not_found(obj: any) -> int:
    if obj and not isinstance(float("nan"), type(obj)):
        print("Type not Found")
        return 1
    match obj:
        case None:
            print(f"Nothing : {obj} {type(obj)}")
        case float():
            print(f"Cheese : {obj} {type(obj)}")
        case bool():
            print(f"Fake : {obj} {type(obj)}")
        case int():
            print(f"Zero : {obj} {type(obj)}")
        case str():
            print(f"Empty : {obj} {type(obj)}")
        case _:
            print("Type not Found")
            return 1
    return 0
