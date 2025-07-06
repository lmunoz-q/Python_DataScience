class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for i, j in zip(V1, V2):
            res += i * j
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [i + j for i, j in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [i - j for i, j in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
