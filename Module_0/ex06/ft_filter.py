

def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None, return
    the items that are true."""
    if function is None:
        def function(a):
            return a is True

    return (a for a in iterable if function(a))


if __name__ == '__main__':
    """example of use"""

    data = [1, 2, 3, 4, 5, 6]

    def check_even(a):
        return a % 2 == 0

    result = ft_filter(check_even, data)
    print(type(result))
    print(result)
    print(list(result))

    result_true = filter(check_even, data)
    print(type(result_true))
    print(result_true)
    print(list(result_true))
