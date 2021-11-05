class Matrix:
    def __init__(self,matrix=[]):
        self.matrix = matrix
    def __str__(self):
        msg=''
        for row in self.matrix:
            for col in row:
               msg=f'{msg}\t{col}'
            msg=f'{msg}\n'
        return msg
    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j]
                        for j in range (len(self.matrix[0]))] for i in range(len(self.matrix))])
a = Matrix([[3,4],[5,6],[7,8]])
b = Matrix([[7,13],[5,6],[13,10]])
c = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f'Матрица A \n{a}')
print(f'Матрица B \n{b}')
print(f'Матрица C \n{c}')
print(f'Матрица A+B \n{a+b}')


