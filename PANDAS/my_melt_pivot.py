import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 89],
    'English': [88, 85, 94]
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)

df_melted = df.melt(id_vars=["Name"], value_vars=["Math", "Science", "English"],
                    var_name="Subject", value_name="Score")

print("\n--- Data after using melt (wide → long) ---")
print(df_melted)

df_pivoted = df_melted.pivot(index="Name", columns="Subject", values="Score")

print("\n--- Data after using pivot (long → wide) ---")
print(df_pivoted)