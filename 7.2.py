import numpy as np
import numpy.random as rand

data = np.zeros((8, 8)) # Создаём нулевую матрицу 8x8 
data[::2, 1::2] = 1 # В каждой нечётной строке каждый чётный элемент заменяем на 1
data[1::2, ::2] = 1 # В каждой чётной строке каждый нечётный элемент меняем на 1

print(data) # Выводим
del data