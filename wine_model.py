import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import joblib
# Load CSV with semicolon separator
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
X = df.drop('quality', axis=1)  # Features
y = df['quality']               # Target variable
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.3f}")
print(f"R2 Score: {r2:.3f}")
joblib.dump(pipeline, 'wine_quality_model.joblib')
print("Model saved as 'wine_quality_model.joblib'")
