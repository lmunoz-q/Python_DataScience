def callLimit(limit: int):
    """
    Decorator factory that creates a decorator limiting the number
    of calls to a function.

    Args:
        limit (int): The maximum number of allowed calls.

    Returns:
        Callable: A decorator that can be applied to any function
        to restrict its number of calls.
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that wraps the given function to limit its calls.

        Args:
            function (Callable): The function to be decorated.

        Returns:
            Callable: The wrapped function with call limitation.
        """
        def limit_function(*args: any, **kwds: any):
            """
            Wrapped function that checks the call count before executing.

            Args:
                *args: Positional arguments for the original function.
                **kwds: Keyword arguments for the original function.

            Prints:
                Error message if the function is called too many times.
            """
            nonlocal count
            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(f"Error: function {function} call too many times")

        return limit_function
    return callLimiter
