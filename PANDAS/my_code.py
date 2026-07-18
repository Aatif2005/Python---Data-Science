import pandas as pd

s1 = pd.Series([71, 84, 56, 23, 56, 98, 56])
print(type(s1))
print(s1)

s2 = pd.Series([71, 84, 56, 23, 56, 98, 56], index=["Aatif", "Ali", "Ahmed", "Ayesha", "Zainab", "Hassan", "Hina"])
print(s2)