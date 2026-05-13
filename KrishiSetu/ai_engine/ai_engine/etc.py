import pandas as pd

df = pd.read_csv(
    "ai_engine/data_ingestion/data/features/features_weekly.csv",
    parse_dates=["week"]
)

print("Total rows:", len(df))
print("\nNaN fraction per column:")
print(df.isna().mean().sort_values(ascending=False).head(20))

print("\nNDVI anomaly non-null count:")
print(df["ndvi_anomaly"].notna().sum())

print("\nFeature group availability:")
print("NDVI rows:", df[[c for c in df.columns if c.startswith("ndvi")]].notna().all(axis=1).sum())
print("Rain rows:", df[[c for c in df.columns if c.startswith("rainfall")]].notna().all(axis=1).sum())
print("Soil rows:", df[[c for c in df.columns if c.startswith("soil")]].notna().all(axis=1).sum())
print("Temp rows:", df[[c for c in df.columns if c.startswith("temp")]].notna().all(axis=1).sum())
