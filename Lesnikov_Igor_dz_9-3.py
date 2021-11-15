# Реализация класса (работник)
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        el_dict = {
            'wage': int(wage),
            'bonus': int(bonus)
        }
        self.name = name
        self.surname = surname
        self.position = position
        self._income = el_dict


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        txt = f'{self.position} {self.name} {self.surname}'
        return txt

    def get_total_income(self):
        wage = self._income
        wage_result = sum(wage.values())
        return wage_result


worker_result = Position('Иван', 'Иванов', 'Инженер', '20000', '10000')
print(worker_result.get_full_name())
print(worker_result.get_total_income())
