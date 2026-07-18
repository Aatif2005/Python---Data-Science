import numpy as np
arr = np.array([1,2,3,4,5,6])
result = arr ** 2
print(result)
# this vectorization this is faster than looping condition

arr = np.array([1,2,3,4,5])
result = arr + 10
print(result)

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2
print(result)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3])
result = arr1 + arr2
print(result)

data = np.array([[10, 20, 30],
                 [15, 25, 35],
                 [20, 30, 40],
                 [25, 35, 45],
                 [30, 40, 50]])
mean = data.mean(axis = 0)
std = data.std(axis = 0)
normalized_data = (data - mean) / std
print(normalized_data)