class Kletka:
    def __init__(self,cell):
        self.cell = cell
    def __str__(self):
        return f'{self.cell}'
    def __add__(self, other):
        return Kletka(self.cell+other.cell)
    def __sub__(self, other):
        r = self.cell-other.cell
        if r>=0:
            return Kletka(r)
        else:
            return ("error")
    def __mul__(self, other):
        return Kletka(self.cell*other.cell)
    def __floordiv__(self, other):
        return Kletka(self.cell//other.cell)
    def __truediv__(self, other):
        return Kletka(self.cell//other.cell)
    def make_order(self,count=1):
        msg=''
        symbol='*'
        for i in range(self.cell//count):
            msg=f'{msg}\n{symbol*count}'
        msg = f'{msg}\n{symbol*(self.cell%count)}'
        return msg
a=Kletka(12)
b=Kletka(14)
print(f'Клетка A: {a} Клетка В: {b}')
print(f'A-B = {a-b}')
print(f'A+B = {a+b}')
print(f'A*B = {a*b}')
print(f'A/B = {b/a}')
print(a.make_order(5))
print(b.make_order(3))