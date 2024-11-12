
def callLimit(limit: int):
    """limiter : decorator to limit the number of calls of a function"""
    count = 0

    def callLimiter(function):
        nonlocal count

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} called too many times")
            else:
                function()

        return limit_function
    return callLimiter
