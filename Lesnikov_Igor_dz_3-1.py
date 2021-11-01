# Англо-русский переводчик цифр (от 0 до 10)
numbers_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}


# Функция, для перевода с английского на русский
def num_translate(number):
    if number in numbers_dict:
        return numbers_dict[number]
    else:
        return None


print(num_translate('nine'))
