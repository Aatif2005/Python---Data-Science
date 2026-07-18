import pandas as pd
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})
print(employees)

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})
print(departments)

print("\n--- Joining DataFrame ---")
print(pd.merge(employees, departments, on="DeptID"))
print(pd.merge(employees, departments, on="DeptID", how="left"))

print("\n--- Concatenating DataFrames---")
df1 = pd.DataFrame({"Name": ["Alice", "Bob"], "Score": [323,426]})
df2 = pd.DataFrame({"Name": ["Charlie", "David"], "Age": [23,24]})
print(df1)
print(df2)
print(pd.concat([df1, df2]))