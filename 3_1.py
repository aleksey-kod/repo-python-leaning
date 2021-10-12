tratslate= {'zero': 'ноль',
               'one': "один",
               'two': "два",
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять'}
""" Задача 1    """
def num_translate(question):
    return tratslate.get(question)
""" Задача 2    """
def num_translate_adv(question):
    if question[0].isupper():
         return str(tratslate.get(str(question).lower())).capitalize()
    else:
        return tratslate.get(question)
print(num_translate(input("Введите число ")))
print(num_translate_adv(input("Введите число ")))


