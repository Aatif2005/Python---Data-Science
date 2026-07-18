import numpy as np
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90],
                [110, 120, 130]])
flat = arr.flatten()
print(flat[0])
print(flat[3:6])
print(flat[3:])
print(flat[3:13])

arr = np.array([10, 20, 30, 40, 50])
idx = [0, 2, 4]
print(arr[idx])

arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25  # Condition: values greater than 25
print(arr[mask])  # [30 40 50]

sliced = arr[1:4]
sliced[0] = 999
print(arr)  