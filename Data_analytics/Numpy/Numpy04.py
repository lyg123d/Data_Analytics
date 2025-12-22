import numpy as np
# 인덱싱과 슬리이싱

array1 = np.arange(10)
array2 = np.arange(1, 10).reshape(-1, 3)

# print(array1[0:2])
# print(array1[0], end=' ')
# print(array1[1], end=' ')
# print(array1[2])

# print(array1[0:2])
# print(array1[::2])

# print(array2[0, 0:2])
# print(array2[0:2, 0:2])

array1 = np.array([10, 20, 30, 40])
array2 = np.array([[1, 2], [3, 4], [5, 6]])
# print(array1[[0, 2]])
# print(array1[[0, 3]])
# print(array1[[0, 2], 1])
# print(array2[[0,1], 0:2])

arr = np.array([1, 2, 3, 4, 5])

print(arr[arr > 3])
print(arr[(arr > 1) & (arr < 5)])