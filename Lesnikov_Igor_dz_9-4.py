# Реализация базового класса Car и дочерних классов
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self):
        if self.is_police:
            return 'Машина повернула на право'
        else:
            return 'Машина повернула на лево'

    def show_speed(self):
        return f'Машина едет со скоростью {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Машина превысила скорость!'
        else:
            return f'Машина едет со скоростью {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Машина превысила скорость!'
        else:
            return f'Машина едет со скоростью {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = Car('50', 'black', 'Toyota', True)
car_2 = TownCar('50', 'black', 'Toyota', True)
car_3 = SportCar('50', 'black', 'Toyota', True)
car_4 = WorkCar('50', 'black', 'Toyota', True)
car_5 = PoliceCar('50', 'black', 'Toyota', True)
print(f'скорость машины {car_1.speed} км/ч, марка машины {car_1.name}, цвет машины {car_1.color}, {car_1.is_police}')
print(car_1.go())
print(car_1.stop())
print(car_1.turn())
print(car_1.show_speed())
print(car_2.show_speed())
print(car_4.show_speed())
