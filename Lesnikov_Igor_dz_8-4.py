# Декоратор позволяющий валидировать входные значения функции
def val_checker(check_func):
    def checker_wrapper(calc_cube):
        def checker(*args):
            result = calc_cube(*args)
            meaning = check_func(*args)
            if meaning:
                return result
            else:
                print(f'ValueError: wrong val {args}')
        return checker
    return checker_wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


number = calc_cube(5)
print(number)
