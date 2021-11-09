class IsDigit(Exception):
    def __init__(self, txt):
        self.txt = txt
list_digit=[]
print('Заполнение списка чисел, для завершение ввода необходимо ввести STOP')
while True:
    try:
        inp_A = input("Введите число или STOP: ")
        if not inp_A.isdigit():
            if inp_A.lower()=='stop':
                break
            raise IsDigit('Вы ввели не число. Попробуйте еще раз')
        list_digit.append(inp_A)
    except IsDigit as err:
            print(err)
print('Введенный список:')
print(*list_digit)
