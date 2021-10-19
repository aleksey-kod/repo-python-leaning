from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'

]
tut_klass = (i for i in zip_longest(tutors, klasses))
print(type(tut_klass))
print(*(tut_klass))
