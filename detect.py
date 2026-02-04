import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Load latest metrics
df = pd.read_csv("metrics.csv")
latest = df.iloc[-1:]

X = latest[["runtime", "cpu_user", "cpu_system", "peak_memory"]]

pred = model.predict(X)

if pred[0] == -1:
    print("Anomalous / high-impact build detected")
else:
    print("Sustainable build")
