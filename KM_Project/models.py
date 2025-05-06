import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load data
df = pd.read_excel("Citation Data.xlsx")

# Clean and engineer features
df["Abstract"] = df["Abstract"].astype(str).fillna("")
df["Abstract Length"] = df["Abstract"].apply(lambda x: len(x.split()))
df["Citations"] = df["Times Cited, All Databases"].fillna(0).astype(int)

# Select features
features = ["Abstract Length", "Research Areas"]
target = "Citations"

X = df[features]
y = df[target]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define numeric and categorical preprocessing
numeric_features = ["Abstract Length"]
categorical_features = ["Research Areas"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

# ----------------------
# Linear Regression
# ----------------------
lr_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
], memory=None)

lr_pipeline.fit(X_train, y_train)
y_pred_lr = lr_pipeline.predict(X_test)

print("\n📊 Linear Regression Performance:")
print("R² Score:", r2_score(y_test, y_pred_lr))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_lr)))

# ----------------------
# Random Forest Regressor
# ----------------------
rf_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, max_features="sqrt", min_samples_leaf=1, random_state=42))
], memory=None)

rf_pipeline.fit(X_train, y_train)
y_pred_rf = rf_pipeline.predict(X_test)

print("\n🌲 Random Forest Performance:")
print("R² Score:", r2_score(y_test, y_pred_rf))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_rf)))

# ----------------------
# Visualize Predictions
# ----------------------
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_rf, alpha=0.6, color='green', label='Random Forest')
plt.scatter(y_test, y_pred_lr, alpha=0.4, color='blue', label='Linear Regression')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Citations")
plt.ylabel("Predicted Citations")
plt.title("Predicted vs Actual Citation Counts")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
