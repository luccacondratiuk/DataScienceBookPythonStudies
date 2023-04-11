import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'Matriz: \n{matrix}')
print(f'Formato: {matrix.shape}')
print(f'Primeiro Elemento: {matrix[0][0]}')
print(f'Último Elemento: {matrix[2][2]}')
print(f'Matriz identidade: \n{np.eye(3,3)}')
