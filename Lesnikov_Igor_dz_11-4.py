# Реализация проекта «Склад оргтехники»

class Warehouse:

    def __init__(self, name, number_of_seats):
        reception_dict = {

        }
        self.name = name
        self.number_of_seats = number_of_seats
        self.reception_dict = reception_dict

    def reception(self, name, number_of_seats):
        if type(name) == int:
            return print('Введите текстовое наименование оборудования!')
        elif type(number_of_seats) == str:
            return print('Введите числовое значения количества едениц оборудования')
        self.reception_dict.update({name: number_of_seats})
        print(self.reception_dict)

    def issue(self, name):
        if int(name):
            print('Введите текстовое наименование оборудования!')
        self.reception_dict.pop(name)
        print(self.reception_dict)


class Office_equipment(Warehouse):
    def __init__(self, name, model, colour, number_of_seats):
        super().__init__(name, number_of_seats)
        self.name = name
        self.model = model
        self.colour = colour


class Printer(Office_equipment):
    def __init__(self, specifications, print_speed, color_print, duplex_printing, name, model, colour, number_of_seats):
        super().__init__(name, model, colour, number_of_seats)
        self.specifications = specifications
        self.print_speed = print_speed
        self.color_print = color_print
        self.duplex_printing = duplex_printing


class Scanner(Office_equipment):
    def __init__(self, specifications, resolution, scan_speed, supported_format, name, model, colour, number_of_seats):
        super().__init__(name, model, colour, number_of_seats)
        self.specifications = specifications
        self.resolution = resolution
        self.scan_speed = scan_speed
        self.supported_format = supported_format


class Copier(Office_equipment):
    def __init__(self, specifications, original_size, copy_speed, resource, name, model, colour, number_of_seats):
        super().__init__(name, model, colour, number_of_seats)
        self.specifications = specifications
        self.original_size = original_size
        self.copy_speed = copy_speed
        self.resource = resource


x = Warehouse('Printer', 2)
x.reception('Printer', 2)


