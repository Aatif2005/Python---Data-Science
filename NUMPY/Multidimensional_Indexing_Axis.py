import numpy as np
arr = np.array([[1,2,3],
[4,5,6],
[7,8,9]])
np.sum(arr,axis = 1)
print(arr[0][1])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
# Accessing an element
print(arr[1, 2])
print(arr[0:2, 1:3])

arr3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
print(arr3D.shape)
print(arr3D[:,0,:])

first_col = arr[:,0]
print(first_col)

arr[:,1] = 0
print(arr3D)