# Декоратор для логирования типов позиционных аргументов
def type_logger(verbosity=0):
    def logger_wrapper(calc_cube):
        def wrapper(*args):
            result = calc_cube(*args)
            if verbosity >= 0:
                type_meaning = f'{", ".join(map(str, args))}: {type(result)}'
            return type_meaning

        return wrapper

    return logger_wrapper


@type_logger(0)
def calc_cube(x, y):
    return x, y ** 3


print(calc_cube(5, 6))


