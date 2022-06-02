import numpy as np
import numpy.random as rand

a, b = rand.sample((5,5)), rand.sample((5,5))

for index in range(len(a.flat)): # flat - перевести многомерный массив в одномерный
    if a.flat[index] < b.flat[index]: # Здесь проходит по двум массивам и сравнивает элементы между собой
        a.flat[index] = 0 # Элемент заменяется на ноль, если элемент в a меньше, чем в b


print(a)

a[0:2] = np.apply_along_axis(np.sin, axis=1, arr=a[0:2])
a[2:4] = np.apply_along_axis(np.cos, axis=1, arr=a[2:4])
a[4:] = np.apply_along_axis(np.exp, axis=1, arr=a[4:])
        
print(a)


# 4. Создать два массива 5x5 со случайными значениями. Сравнить полученные массивы между собой, 
# обнулить значения элементов первого массива, которые являются меньше значений элементов второго 
# массива. Для первых двух строк вычислить sin, для следующих двух вычислить cos и для последней 
# строки вычислить exp. 