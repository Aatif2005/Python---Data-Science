import pandas as pd
s1 = pd.Series([71, 56,32,45,67,89,44])
print(type(s1))
print(s1)
s2= pd.Series([71, 56,32,45,67,89,44], index = ["Aatif", "Harry", "Subh","Rohan","Akash","Kirti","Jhon"])
print(s2)
print(s2["Aatif"])