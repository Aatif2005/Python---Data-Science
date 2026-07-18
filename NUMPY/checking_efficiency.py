import sys
import numpy as np

# Define the data OUTSIDE the comment
list_data = list(range(1000))
numpy_data = np.array(list_data)

# Size comparison
print("Python list size:", sys.getsizeof(list_data) * len(list_data), "bytes")
print("NumPy array size:", numpy_data.nbytes, "bytes")

# Python list (loop-based)
list_squares = [x ** 2 for x in list_data]

# NumPy (vectorized)
numpy_squares = numpy_data ** 2

print("List squares (first 5):", list_squares[:5])
print("NumPy squares (first 5):", numpy_squares[:5])