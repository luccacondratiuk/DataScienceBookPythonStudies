import numpy as np

height_weight_age = np.array([70,170,40])   # Array simples de três dimensões

print(height_weight_age)
v = np.array([1,2,3])
w = np.array([4,5,6])
print(f'V: {v}')
print(f'W: {w}')
print(f'Soma de vetores (V+W): {np.add(v,w)}')
print(f'Subtração de vetores (V-W): {np.subtract(v,w)}')
print(f'Produto escalar (2*W): {2*v}')
print(f'Média(v): {v.mean()}')
print(f'Produto Vetorial(V*W): {v.dot(w)}')
print(f'Módulo: {np.sqrt(v.dot(v))}')
print(f'Distância: {np.sqrt(np.subtract(v,w).dot(np.subtract(v,w)))}')
