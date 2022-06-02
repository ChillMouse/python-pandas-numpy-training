import numpy as np
import numpy.random as rand

l_matrix, s_matrix = rand.randint(0, 1000, (5, 3)), rand.randint(0, 1000, (3, 2))

print(l_matrix)
s_matrix = np.column_stack((s_matrix,np.zeros((3, 1))))
s_matrix = np.row_stack((s_matrix,np.zeros((2, 3))))
print(s_matrix)
print(l_matrix + s_matrix)