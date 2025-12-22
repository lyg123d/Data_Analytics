import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array2 = np.arange(6)
array3 = np.arange(1, 11)
array4 = np.array([[1, 2, 3, 4, 5 ], [6, 7, 8, 9, 10]])


print(array1.shape)
print(array2.shape)
print(array3.shape)

print(array1.ndim)

print(array1.size)
print(array2.size)

print(array4.dtype)
print(array2.dtype)

print(len(array4))
