import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array2 = np.arange(10)

# print(array1.reshape((3, 3)))
# print(array2.reshape((-1, 5)))

array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array3.ravel())
print(array3)
print(array3.transpose())