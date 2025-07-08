def ft_statistics(*args, **kwargs) -> None:
    len_args = len(args)
    moyenne = 0
    for i in args:
        moyenne += i
    moyenne /= len_args
    if "mean" in kwargs.values():
        print(f"mean : {moyenne}")

