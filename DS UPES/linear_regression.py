# SIMPLE LINEAR REGRESSION FROM SCRATCH
# Predict car selling price using km_driven

import pandas as pd
import matplotlib.pyplot as plt
import math

# Step 1: Load Dataset
data = pd.read_csv(r"C:\Users\aatif\OneDrive\Desktop\cardekho_dataset.csv")

print("Dataset:")
print(data.head())

# Step 2: Select Independent and Dependent Variables

X = data["km_driven"]
Y = data["selling_price"]

# Step 3: Remove Missing Values

df = pd.DataFrame({
    "X": X,
    "Y": Y
})

df = df.dropna()

X = df["X"].tolist()
Y = df["Y"].tolist()

# Step 4: Split Data into Training and Testing

split = int(0.8 * len(X))

X_train = X[:split]
Y_train = Y[:split]

X_test = X[split:]
Y_test = Y[split:]

# Step 5: Calculate Required Summations

n = len(X_train)

sum_x = sum(X_train)
sum_y = sum(Y_train)

sum_xy = sum(
    X_train[i] * Y_train[i]
    for i in range(n)
)

sum_x2 = sum(
    x ** 2 for x in X_train
)

# Step 6: Calculate Slope (m)

m = (
    (n * sum_xy - sum_x * sum_y)
    /
    (n * sum_x2 - sum_x ** 2)
)

# Step 7: Calculate Intercept (c)

c = (sum_y - m * sum_x) / n

print("\nLinear Regression Model")
print("-----------------------")

print("Slope (m):", m)
print("Intercept (c):", c)

print("\nRegression Equation:")
print("Selling Price =", m, "* km_driven +", c)

# Step 8: Make Predictions

predictions = []

for x in X_test:
    y_pred = m * x + c
    predictions.append(y_pred)

# Step 9: Compare Actual and Predicted Values

results = pd.DataFrame({
    "Actual Price": Y_test,
    "Predicted Price": predictions
})

print("\nActual vs Predicted Values:")
print(results.head(10))

# Step 10: Calculate Mean Absolute Error (MAE)

mae = sum(
    abs(Y_test[i] - predictions[i])
    for i in range(len(Y_test))
) / len(Y_test)

# Step 11: Calculate Mean Squared Error (MSE)

mse = sum(
    (Y_test[i] - predictions[i]) ** 2
    for i in range(len(Y_test))
) / len(Y_test)

# Step 12: Calculate Root Mean Squared Error (RMSE)

rmse = math.sqrt(mse)

# Step 13: Calculate R-Squared

mean_y = sum(Y_test) / len(Y_test)

ss_total = sum(
    (y - mean_y) ** 2 for y in Y_test
)

ss_residual = sum(
    (Y_test[i] - predictions[i]) ** 2
    for i in range(len(Y_test))
)

r2 = 1 - (ss_residual / ss_total)

print("\nModel Evaluation")
print("-----------------------")

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R-Squared:", r2)

# Step 14: Visualize Results

plt.figure(figsize=(10, 6))

plt.scatter(
    X_test,
    Y_test,
    label="Actual Prices",
    alpha=0.5
)

plt.plot(
    X_test,
    predictions,
    color="red",
    label="Regression Line"
)

plt.xlabel("Kilometres Driven")
plt.ylabel("Selling Price")

plt.title("Simple Linear Regression - Car Price Prediction")

plt.legend()
plt.show()

# Step 15: Predict Price for a New Car

new_km = 50000

predicted_price = m * new_km + c

print("\nNew Car Prediction")
print("-----------------------")

print("Kilometres Driven:", new_km)

print("Predicted Selling Price:",
      round(predicted_price, 2))
