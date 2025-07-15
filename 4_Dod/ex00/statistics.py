def quarted(sorted_list: list, quartile: int) -> float:
    n = len(sorted_list)
    index = 0
    if quartile == 25:
        index = (n - 1) / 4
    if quartile == 75:
        index = (3 * (n - 1)) / 4
    if quartile == 50:
        index = (n - 1) / 2
    decimal = index % 1
    if decimal == 0:
        return sorted_list[int(index)]
    else:
        return (sorted_list[int(index)] * (1 - decimal)) +\
               (decimal * sorted_list[int(index) + 1])


def variation(sorted_list: list, moyenne: float) -> float:
    ret = 0
    for i in sorted_list:
        ret += (i - moyenne) ** 2
    return (ret / len(sorted_list))


def ft_statistics(*args: any, **kwargs: any) -> None:
    if not args:
        print("ERROR")
        return
    lst = []
    for i in args:
        lst.append(float(i))
    lst.sort()
    len_args = len(args)
    moyenne = 0
    for i in lst:
        moyenne += i
    if len_args > 0:
        moyenne /= len_args
    if "mean" in kwargs.values():
        print(f"mean : {moyenne}" if len_args else "ERROR")
    if "median" in kwargs.values():
        print(f"median : {quarted(lst, 50)}" if len_args > 0 else "ERROR")
    if "quartile" in kwargs.values():
        print(f"quartile : [{quarted(lst, 25)}, {quarted(lst, 75)}]"
              if len_args > 0 else "ERROR")
    if "std" in kwargs.values():
        print(f"std : {variation(lst, moyenne) ** 0.5}"
              if len_args > 0 else "ERROR")
    if "var" in kwargs.values():
        print(f"var : {variation(lst, moyenne)}" if len_args > 0 else "ERROR")
