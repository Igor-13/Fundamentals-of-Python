# Реализация класса-исключения

class Division:

    def __floordiv__(self, other, other_2):
        self.other = other
        self.other_2 = other_2

    def div(cls, other, other_2):
        try:
            result = other // other_2
            print(result)
        except ZeroDivisionError:
            print("На ноль делить нельзя!")


x = Division()
x.div(5, 0)


