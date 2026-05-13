import os
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from ml.experts.vegetation_expert import VegetationExpert
from ml.experts.rainfall_expert import RainfallExpert
from ml.experts.soil_expert import SoilExpert
from ml.experts.temperature_expert import TemperatureExpert


MODEL_PATH = "models/fusion.pkl"


def train(df):
    veg = VegetationExpert()
    rain = RainfallExpert()
    soil = SoilExpert()
    temp = TemperatureExpert()

    # Prepare empty score arrays
    n = len(df)
    veg_scores = np.full(n, np.nan)
    rain_scores = np.full(n, np.nan)
    soil_scores = np.full(n, np.nan)
    temp_scores = np.full(n, np.nan)

    # Vegetation
    ndvi_cols = [c for c in df.columns if c.startswith("ndvi")]
    ndvi_mask = df[ndvi_cols].notna().all(axis=1)
    if ndvi_mask.any():
        veg_scores[ndvi_mask] = veg.model.predict(df.loc[ndvi_mask, ndvi_cols])

    # Rainfall
    rain_cols = [c for c in df.columns if c.startswith("rainfall")]
    rain_mask = df[rain_cols].notna().all(axis=1)
    if rain_mask.any():
        rain_scores[rain_mask] = rain.model.predict_proba(
            df.loc[rain_mask, rain_cols]
        )[:, 1]

    # Soil
    soil_cols = [c for c in df.columns if c.startswith("soil")]
    soil_mask = df[soil_cols].notna().all(axis=1)
    if soil_mask.any():
        soil_scores[soil_mask] = soil.model.predict(
            df.loc[soil_mask, soil_cols]
        )

    # Temperature
    temp_cols = [c for c in df.columns if c.startswith("temp")]
    temp_mask = df[temp_cols].notna().all(axis=1)
    if temp_mask.any():
        temp_scores[temp_mask] = temp.model.predict(
            df.loc[temp_mask, temp_cols]
        )

    # Build fusion matrix
    X_fusion = np.column_stack([
        veg_scores,
        rain_scores,
        soil_scores,
        temp_scores
    ])

    # Proxy target
    y_target = df["ndvi_anomaly"].shift(-2).values

    # Keep rows where at least 2 modalities exist
    valid_mask = np.sum(~np.isnan(X_fusion), axis=1) >= 2
    valid_mask &= ~np.isnan(y_target)

    X_fusion = X_fusion[valid_mask]
    y_target = y_target[valid_mask]

    # Replace remaining NaNs with 0 (neutral contribution)
    X_fusion = np.nan_to_num(X_fusion, nan=0.0)

    assert len(X_fusion) > 30, (
        f"❌ Not enough fusion samples after relaxed alignment: {len(X_fusion)}"
    )

    model = LinearRegression(positive=True)
    model.fit(X_fusion, np.abs(y_target))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"✅ Fusion model trained on {len(X_fusion)} samples")


if __name__ == "__main__":
    df = pd.read_csv(
        "data_ingestion/data/features/features_weekly.csv",
        parse_dates=["week"]
    )

    train(df)
