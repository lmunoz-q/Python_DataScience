def ft_filter(function, iterable):
    """
    Filter elements of an iterable using a function without using the built-in filter function.

    Args:
        function (callable): A function that returns True or False for each element.
        iterable (iterable): The iterable to be filtered.

    Returns:
        list: A list containing the elements from iterable for which function returns True.
    """
    return [x for x in iterable if function(x)]