# feature_engineering/anomalies.py

import pandas as pd
from feature_engineering.config import GROUP_COLS, TRAIN_YEARS


def compute_baselines(df: pd.DataFrame) -> pd.DataFrame:
    train_df = df[df["week"].dt.year.isin(TRAIN_YEARS)]

    baselines = (
        train_df
        .groupby(GROUP_COLS)
        .agg(
            ndvi_baseline=("ndvi", "mean"),
            soil_baseline=("soil_moisture", "mean"),
            temp_baseline=("temp_c", "mean"),
        )
        .reset_index()
    )

    return baselines


def add_anomalies(df: pd.DataFrame, baselines: pd.DataFrame) -> pd.DataFrame:
    df = df.merge(baselines, on=GROUP_COLS, how="left")

    df["ndvi_anomaly"] = df["ndvi"] - df["ndvi_baseline"]
    df["soil_moisture_anomaly"] = df["soil_moisture"] - df["soil_baseline"]
    df["temp_anomaly"] = df["temp_c"] - df["temp_baseline"]

    return df
