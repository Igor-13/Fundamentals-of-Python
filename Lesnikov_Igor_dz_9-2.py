# Реализация класса дорога (расчёт массы асфальта)
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        weight = 25
        thickness = 5
        result = _length * _width * weight * thickness
        result_txt = f'{result // 1000} т.'
        self.result_txt = result_txt


result_road = Road(20, 5000)
print(result_road.result_txt)
