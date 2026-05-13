# feature_engineering/run_features.py

import pandas as pd

from feature_engineering.rolling_features import add_rolling_features
from feature_engineering.anomalies import compute_baselines, add_anomalies
from feature_engineering.trends import add_trend_features


# ---------------- LOAD ---------------- #

df = pd.read_csv(
    "data_ingestion/data/aligned/aligned_weekly.csv",
    parse_dates=["week"]
)

# ---------------- ROLLING FEATURES ---------------- #

df = add_rolling_features(df)

# ---------------- BASELINES & ANOMALIES ---------------- #

baselines = compute_baselines(df)
df = add_anomalies(df, baselines)

# ---------------- TRENDS ---------------- #

df = add_trend_features(df)

# ---------------- SAVE ---------------- #

df.to_csv("data_ingestion/data/features/features_weekly.csv", index=False)

print("✅ Feature engineering complete")
