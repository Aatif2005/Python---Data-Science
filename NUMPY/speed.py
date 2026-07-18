'''import numpy as np
import time

size = 1_000_000

# NumPy approach (fast)
start = time.time()
l1 = np.array(list(range(size)))
l2 = np.array(list(range(size)))
add = l1 + l2
end = time.time()
print("NumPy time:", end - start)

# Python list approach (for comparison)
start = time.time()
l1 = list(range(size))
l2 = list(range(size))
add = [x + y for x, y in zip(l1, l2)]
end = time.time()
print("List time:", end - start)'''

import numpy as np
import time

size = 1_000_000

# Create data BEFORE timing
l1_list = list(range(size))
l2_list = list(range(size))
l1_np = np.array(l1_list)
l2_np = np.array(l2_list)

# Time NumPy (addition only)
start = time.time()
add = l1_np + l2_np
end = time.time()
print("NumPy time:", end - start)

# Time List (addition only)
start = time.time()
add = [x + y for x, y in zip(l1_list, l2_list)]
end = time.time()
print("List time:", end - start)