
def set_sum(dataset):
    """return the sum of a dataset"""
    result = 0
    for elt in dataset:
        result += elt
    return result


def mean_r(dataset):
    """returns the mean of a dataset"""
    return set_sum(dataset) / len(dataset)


def mean(dataset):
    """displays the median of a dataset"""
    print(f"mean : {mean_r(dataset)}")


def median(dataset):
    """displays the median of a dataset"""
    tmp = sorted(dataset)
    n = len(dataset)
    if n % 2 == 1:
        print(f"median : {tmp[(n // 2)]}")
    else:
        print(f"median : {(tmp[n // 2] + tmp[(n // 2) - 1]) // 2}")


def quartile(dataset):
    """displays the first and third quartiles of a dataset"""
    tmp = sorted(dataset)
    n = len(dataset)
    first = int(n * 1/4)
    third = int(n * 3/4)
    print(f"quartiles : {[tmp[first], tmp[third]]}")


def var_r(dataset):
    """returns the variance of a dataset"""
    result = 0
    m = mean_r(dataset)
    for elt in dataset:
        result += (elt - m) ** 2
    result /= len(dataset)
    return result


def var(dataset):
    """displays the variance of a dataest"""
    print(f"var : {var_r(dataset)}")


def std(dataset):
    """displays the standard deviation of a dataset"""
    result = var_r(dataset)
    result **= 0.5
    print(f"std : {result}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """function to perform statistics operation on an arbitrary
number of integers passed as an argument"""

    if len(args) < 1:
        print("Error no args")
        return
    elif True in [type(x) is not int for x in args]:
        print("Args must be integers")
        return

    for op in kwargs.values():
        match op:
            case "mean":
                mean(args)
            case "median":
                median(args)
            case "quartile":
                quartile(args)
            case "std":
                std(args)
            case "var":
                var(args)
            case _:
                print("Error unknown operation")
