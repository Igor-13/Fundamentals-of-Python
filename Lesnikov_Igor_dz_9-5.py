# Реализация класса канцелярская принадлежность
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки маркером'


stationery_1 = Stationery('канцелярская принадлежность')
stationery_2 = Pen('канцелярская принадлежность')
stationery_3 = Pencil('канцелярская принадлежность')
stationery_4 = Handle('канцелярская принадлежность')
print(stationery_1.draw())
print(stationery_2.draw())
print(stationery_3.draw())
print(stationery_4.draw())
