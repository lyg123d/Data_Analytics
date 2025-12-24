import numpy as np
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr2 = np.arange(1, 11)
print(np.sum(arr1, axis=0))
print(np.sum(arr1, axis=1))

print(np.sum(arr2, axis=0))
# print(np.sum(arr2, axis=1))

print(np.mean(arr1, axis=0))
print(np.mean(arr1, axis=1))

print(np.max(arr1))
print(np.min(arr1))

print(np.max(arr2))
print(np.min(arr2))

print(np.argmax(arr1))
print(np.argmin(arr1))

print(np.argmax(arr2))
print(np.argmin(arr2))