class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt
print('Процедура деления двух чисел A/B')
while True:
    try:
        inp_A = input("Введите число A: ")
        inp_A = int(inp_A)
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз")


while True:
    try:
        inp_B = input("Введите число В: ")
        inp_B = int(inp_B)
        if inp_B == 0:
            raise DivisionZero("Деление на 0 не возможно. Попробуйте еще разrt")
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз")
    except DivisionZero as err:
        print(err)

print(f"Все хорошо. A/B = {inp_A/inp_B}")




