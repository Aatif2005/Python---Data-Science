import numpy as np

# Creating a 1D NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a 2D NumPy array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Checking type and shape
print("Type:", type(arr1))
print("Shape:", arr2.shape)

print(np.zeros((3, 4)))
print(np.ones((3, 5)))
print(np.full((4, 6), 8))
print(np.arange(1, 100, 2))
print(np.linspace(0, 1, 5))

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dimensions:", arr.ndim)
print("Data type:", arr.dtype)

myarr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [110, 120, 130]])
print(myarr)
print("Shape:", myarr.shape)
print("Size:", myarr.size)
print("Dimensions:", myarr.ndim)
print("Data type:", myarr.dtype)

myarr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [110, 120, 130]], dtype = 'float64')
print(myarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

reshaped = arr.reshape((3, 2))
print(reshaped)
flattened = arr.flatten()  # Convert 2D → 1D
print(flattened)  # [1 2 3 4 5 6]