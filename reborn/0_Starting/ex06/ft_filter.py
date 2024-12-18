def ft_filter(function, iterable):
    """
    Filter elements of an iterable with  fucntion wigoutusing th built-in
    filter function.

    Args:
        function (callable): A function that returns True or Flase for earch
        element.
        iterable (iteratable): The iterable to be filtered.

    Returns:
        list: A list containing the elements from iterable for which function
        returns True.
    """
    return [x for x in iterable if function(x)]
