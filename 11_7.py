import re
class ComplexDigit():
    def __init__(self,real,imag):
        self.real=float(real)
        self.imag=float(imag)

    @classmethod
    def complex_from_string(cls, complex_as_str):
        re_complex = re.compile(r'^(?P<real>[+,-]*\d+)(?P<imag>[+,-]\d+(?=i))',re.IGNORECASE)
        if not re_complex.match(complex_as_str):
            raise ValueError(f'не верный формат записи: {complex_as_str}')
        return ComplexDigit(**re.match(re_complex,complex_as_str).groupdict())

    def __add__(self, other):
        return ComplexDigit(self.real+other.real,self.imag+other.imag)
    def __sub__(self, other):
        return ComplexDigit(self.real - other.real, self.imag - other.imag)
    def __str__(self):
        return f'{self.real}+{self.imag}j' if self.imag>=0 else f'{self.real}{self.imag}j'

list_complex=[]
for i in ['3+4i','-18+4i','3+- 4i']:
    try:
        list_complex.append(ComplexDigit.complex_from_string(i))
    except ValueError as err:
        print(err)
b=ComplexDigit(6,5)
print(f'Решение для ({list_complex[0]})+({b})={list_complex[0]+b}')
print(f'Решение для ({list_complex[0]})-({b})={list_complex[0]-b}')
print(f'Решение для ({list_complex[0]})+({list_complex[1]})={list_complex[0]+list_complex[1]}')



