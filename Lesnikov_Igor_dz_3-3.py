import random


# Функция возвращающая n шуток из трёх случайных слов
def get_jokes(number_of_jokes):
    """
    Function that returns n jokes from three random words

    :param number_of_jokes: int
    :return: list
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    idx = number_of_jokes
    result = []
    while idx > 0:
        word_1 = random.choice(nouns)
        word_2 = random.choice(adverbs)
        word_3 = random.choice(adjectives)
        all_word = [f'{word_1} {word_2} {word_3}']
        result.append(all_word)
        nouns.remove(word_1)
        adverbs.remove(word_2)
        adjectives.remove(word_3)
        idx -= 1
    return result


print(get_jokes(3))
