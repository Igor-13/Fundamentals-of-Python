# Скрипт для вывода на экран записанных данных
if __name__ == '__main__':

    import add_sale

    def snow_sale(*args):
        arg = list(args)
        if len(arg) == 0:
            print(add_sale.args_add)
        elif len(arg) == 1:
            print(add_sale.args_add[arg[0]:])
        else:
            print(add_sale.args_add[arg[0]-1:arg[-1]])

snow_sale(1, 3)
