import seaborn as sns
import matplotlib.pyplot as plt  # ✅ added
import pandas as pd
print(sns.get_dataset_names())

tips = sns.load_dataset("tips")
print(tips.head())
print(tips.info())

sns.barplot(x="total_bill", y="tip", data=tips)
plt.title('Line Plot Example')
plt.show()

flights = sns.load_dataset('flights')
pivot_table = flights.pivot(index="month", columns="year", values="passengers")

sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Heatmap of Passengers')
plt.show()

df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 34, 43],
    "salary": [25000, 27000, 52000, 60000, 58000, 62000, 61000, 65000, 38000, 45000],
    "gender": ["M", "F", "M", "F", "F", "M", "M", "F", "F", "M"]
})

sns.scatterplot(x="age", y="salary", hue="gender", data=df)
plt.title('Salary vs Age Scatter Plot')
plt.show()