import os
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from ml.training.targets import vegetation_target

MODEL_PATH = "models/vegetation.pkl"


def train(df):
    # Vegetation-only features
    veg_features = [
        c for c in df.columns
        if c.startswith("ndvi")
    ]

    assert len(veg_features) > 0, "❌ No NDVI features found"

    X = df[veg_features]
    y = vegetation_target(df)

    # Combine & clean
    data = X.copy()
    data["target"] = y
    data = data.dropna()

    X_clean = data[veg_features]
    y_clean = data["target"]

    # Safety checks
    assert len(X_clean) > 100, (
        f"❌ Not enough vegetation samples: {len(X_clean)}"
    )

    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_clean, y_clean)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(
        f"✅ Vegetation model trained on {len(X_clean)} samples "
        f"with features {veg_features}"
    )


if __name__ == "__main__":
    df = pd.read_csv(
        "data_ingestion/data/features/features_weekly.csv",
        parse_dates=["week"]
    )

    train(df)
