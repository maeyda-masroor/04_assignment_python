import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Example dataset
# Replace this with your actual data
data = {
    'X': [1, 2, 3, 4, 5],
    'y': [2, 4, 5, 4, 5]
}
df = pd.DataFrame(data)

# Splitting into features and target
X = df[['X']]  # Feature matrix
y = df['y']    # Target variable

# Train/test split (optional)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a .pkl file
with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as 'linear_regression_model.pkl'")
