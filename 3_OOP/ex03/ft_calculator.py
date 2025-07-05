class calculator:
    def __init__(self, values):
        self.values = values

    def __add__(self, object) -> None:
        for i in range(len(self.values)):
            self.values[i] += object
        print(self.values)

    def __mul__(self, object) -> None:
        for i in range(len(self.values)):
            self.values[i] *= object
        print(self.values)

    def __sub__(self, object) -> None:
        for i in range(len(self.values)):
            self.values[i] -= object
        print(self.values)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError("Divide by 0 is forbidden")
        for i in range(len(self.values)):
            self.values[i] /= object
        print(self.values)
