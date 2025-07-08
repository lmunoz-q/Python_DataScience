def quartilator(sorted_list: list, quartile: int) -> float:
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
        return (sorted_list[int(index)] * (1 - decimal)) + (decimal * sorted_list[int(index) + 1])

def ft_statistics(*args: any, **kwargs: any) -> None:
    sorted_list = []
    for i in args:
        sorted_list.append(float(i))
    sorted_list.sort()
    len_args = len(args)
    moyenne = 0
    for i in sorted_list:
        moyenne += i
    moyenne /= len_args
    if "mean" in kwargs.values():
        print(f"mean : {moyenne}")
    print(f"median : {quartilator(sorted_list, 50)}")
    print(f"quartile : [{quartilator(sorted_list, 25)}, {quartilator(sorted_list, 75)}]")
