# Реализация класса "Дата"

class Data:

    def __init__(self, param):
        self.param = param

    @classmethod
    def conversion(cls, param):
        numbers_1 = []
        number_x = param.split("-")
        for number in number_x:
            number = int(number)
            numbers_1.append(number)
        return numbers_1
    @staticmethod
    def validation(numbers_1):
        for z in numbers_1:
            if z == numbers_1[0] and 1 <= z <= 31:
                continue
            elif z == numbers_1[1] and 1 <= z <= 12:
                continue
            elif z == numbers_1[2] and 2020 <= z <= 2020:
                continue
            else:
                print('ведите корректную дату')
        print('Дата введена верно!')


x = Data.conversion('10-1-2020')
Data.validation(x)


