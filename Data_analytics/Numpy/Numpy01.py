import numpy as np

#Numpy배열 생성법
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array2 = np.arange(6)
array3 = np.arange(1, 11)

np.zeros(3)
np.zeros((2, 3))
np.ones((2, 3))  
np.ones(3) 
np.full((2, 2), 7)


array4 = np.linspace(1, 10, 10, endpoint=False)

print(array4.shape)