import numpy as np
import numpy.random as rand

#1
data = rand.randint(0, 1000, (10, 10)) # Создаём матрицу с числами от 0 до 10 размером 10x10


print(data)

print(f'Минимум: {data.min()}')

print(f'Максимум: {data.max()}')
del data