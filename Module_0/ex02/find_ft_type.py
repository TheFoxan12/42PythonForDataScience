
def all_thing_is_obj(obj: any) -> int:
    match obj:
        case list():
            print("List : " + str(type(obj)))
        case tuple():
            print("Tuple : " + str(type(obj)))
        case set():
            print("Set : " + str(type(obj)))
        case dict():
            print("Dict : " + str(type(obj)))
        case "Brian":
            print("Brian is in the kitchen : " + str(type(obj)))
        case "Toto":
            print("Toto is in the kitchen : " + str(type(obj)))
        case _:
            print("Type not found")
    return 42
