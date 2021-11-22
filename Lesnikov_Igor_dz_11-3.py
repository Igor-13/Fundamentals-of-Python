# Реализация класса-исключения на проверку чисел

class Number:

    def __init__(self, meaning):
        self.meaning = meaning

    def examination(self, meaning):
        result = []
        while meaning != 'stop':
            try:
                meaning = input('Введите значение')
                meaning = int(meaning)
                result.append(meaning)
            except ValueError:
                print("Введите другое значение")
        print(result)


z = Number(5)
z.examination(5)
