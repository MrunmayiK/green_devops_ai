import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load data
df = pd.read_csv("dataset.csv")

X = df[["runtime", "cpu_user", "cpu_system", "peak_memory"]]

# Train anomaly detector
model = IsolationForest(
    contamination=0.15,
    random_state=42
)

model.fit(X)

joblib.dump(model, "model.pkl")

print("Model trained on", len(X), "samples")
