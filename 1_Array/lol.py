def compress_string(s: str) -> None:
    if s is not None:
        l = 0
        j = s[0]
        ret = ""
        for i in s:
            if i == j:
                l += 1
            else:
                ret += j + str(l)
                l = 1
                j = i
    print(ret)


def main():
    compress_string("abccc")

if __name__ == "__main__":
    main()
