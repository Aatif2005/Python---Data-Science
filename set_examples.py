set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union – combines all unique elements
print(set1 | set2)            # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))       # same result

# Intersection – common elements
print(set1 & set2)            # {3, 4}
print(set1.intersection(set2))# same result

# Difference – in set1 but not in set2
print(set1 - set2)            # {1, 2}
print(set1.difference(set2))  # same result

# Symmetric Difference – in either set, but not both
print(set1 ^ set2)                     # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))# same result