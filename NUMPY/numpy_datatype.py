import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array([1.5, 2.7, 3.9])
print(arr.dtype)

arr_int = arr.astype(np.int32)
print(arr_int)
print(arr.dtype)
arr_float = arr.astype(np.float32)
print(arr_float)

arr_large = np.array([100000, 2000000, 3000000],
dtype = np.int64)
arr_small = arr_large.astype(np.int32)
print(arr_small)
print(arr_small.dtype)

arr_int64 = np.array([1, 2, 3], dtype=np.int64)
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
print(arr_int64.nbytes)
print(arr_int32.nbytes)

arr = np.array(['apple', 'banana', 'cherry'], dtype='U10')  # Unicode string array
print(arr)

arr = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype='complex128')
print(arr)

arr = np.array([{'a': 1}, [1, 2, 3], 'hello'], dtype=object)
print(arr)