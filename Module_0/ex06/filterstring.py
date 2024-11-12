import sys
from ft_filter import ft_filter


def filterstring():
    """\
small program that filters a string
    output:
        a list of words from S that have a length greater than N
    inputs:
        S a string
        N an integer
    """
    args = sys.argv
    if len(args) != 3:
        print("AssertionError: need 2 arguments")
        return

    s = args[1]
    try:
        s = int(s)
    except ValueError:
        pass
    else:
        print("AssertionError: first argument needs to be a string")
        return

    try:
        n = int(args[2])
    except ValueError:
        print("AssertionError: second argument needs to be an integer")
        return

    print([word for word in ft_filter(
        lambda x: len(x) > n,
        s.split(' ')
    )])


if __name__ == '__main__':
    filterstring()
