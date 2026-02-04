import pandas as pd

df = pd.read_csv("metrics.csv")

print("Dataset size:", len(df))
print(df.describe())

df.to_csv("dataset.csv", index=False)
