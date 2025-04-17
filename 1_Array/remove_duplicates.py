def remove_duplicates(lst: list) -> list:
    j = 0
    for i in lst:
        print(i)
        a = i
        for x in lst:
            if x == a:
                j += 1
            if j > 1:
                while j > 1:
                    lst.remove(a)
                    j -= 1
        j = 0
    return lst

def main():
    print(remove_duplicates([1, 2, 2, 3, 1]))        # [1, 2, 3]
    print(remove_duplicates(["a", "b", "a", "c"]))  # ['a', 'b', 'c']
    print(remove_duplicates([]))                    # []
    print(remove_duplicates(["x", "x", "x"]))        # ['x']

if __name__ == "__main__":
    main()
