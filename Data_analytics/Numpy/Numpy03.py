import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array2 = np.arange(10)

# print(array1.reshape((3, 3)))
# print(array2.reshape((-1, 5)))

array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array3.ravel()) # 1차원으로 펼침
print(array3)
print(array3.transpose()) # 행과 열의 위치를 변경