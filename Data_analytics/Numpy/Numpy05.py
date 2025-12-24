import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)

#스칼라 브로드캐스팅
arr = np.array([1, 2, 3])

# print(arr + 10)
# print(arr * 2)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# print(arr + np.array([10, 20, 30]))
print(arr + np.array([[10], [20]]))