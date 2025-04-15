def compress_string(s: str) -> str:
    if not s:
        return s

    l = 1
    j = s[0]
    ret = []
    for i in range(1, len(s)):
        if s[i] == j:
            l += 1
        else:
            ret.append(j + str(l))
            l = 1
            j = s[i]
    ret.append(j + str(l))
    compressed = ''.join(ret)
    return compressed if len(compressed) < len(s) else s


def main():
    print(compress_string("abccc"))

if __name__ == "__main__":
    main()
