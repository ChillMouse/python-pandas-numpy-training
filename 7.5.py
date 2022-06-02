import numpy as np
import numpy.random as rand

a = rand.randint(100, 1001, (8, 3))
print(a)
a.sort()
a = a.T
print(a)
print(a.mean())
print(a.sum(axis=1))
print(a.sum(axis=0))


    # 5. Создать массив 8x3 случайных элементов с начальным значением 100 
    # конечным значением 1000, отсортировать значения и выполнить транспонирование массива. 
    # Вычислить среднее значение и сумму элементов по строкам и столбцам. 