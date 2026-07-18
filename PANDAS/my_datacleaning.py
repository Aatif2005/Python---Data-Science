import pandas as pd

df = pd.read_csv(r"C:\Users\aatif\OneDrive\Desktop\data_cleaning_practice.csv")

print("--- Original DataFrame ---")
print(df)

print("\n--- Null Check (True/False) ---")
print(df.isnull())

print("\n--- Null Count per Column ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows (True/False) ---")
print(df.duplicated())

# This saves the result back into df
df = df.drop_duplicates()

print("\n--- After Removing Duplicates ---")
print(df)

print("\n--- After Removing Duplicates in Name and Age---")
print(df.duplicated(subset=["name", "age"]))

print("\n--- Finding State name ---")
print(df["city"].str.contains("delhi", case = False))

print("\n--- Spliting Emails ---")
print(df["email"].str.split("@"))
print(type(df["email"].str.split("@")[0]))

print("\n--- Type conversion ---")
df2 = df.dropna().copy()
df2["age"] = df2["age"].astype(int)
print(df2)
print(df2.info())

print("\n--- Applying Functions ---")
df2["age group"] = df2["age"].apply(lambda x : "adult" if x >= 25 else "minor")
print(df2)
print("\n--- Map functions---")
gender_map = {"M" : "male", "F" : "female", "O" : "others"}
df2["gender"] = df2["gender"].map(gender_map)
print(df2)