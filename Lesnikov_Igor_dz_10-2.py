# Реализация класса одежда
from abc import abstractmethod


class Clothes:

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.__v = v

    def tissue_consumption(self):
        return self.__v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.__h = h

    def tissue_consumption(self):
        return 2 * self.__h + 0.3


class MyContainer:
    def __init__(self, *args):
        self.__subobjects = args

    def tissue_consumption(self):
        sum = 0
        for subobject in self.__subobjects:
            sum += subobject
        return f'Количество ткани: {sum:.2f}'

a = Clothes()
clothes_coat = Coat(10)
clothes_coat_1 = clothes_coat.tissue_consumption()
clothes_costume = Costume(20)
clothes_costume_1 = clothes_costume.tissue_consumption()
things = MyContainer(clothes_coat_1, clothes_costume_1)
print(things.tissue_consumption())


