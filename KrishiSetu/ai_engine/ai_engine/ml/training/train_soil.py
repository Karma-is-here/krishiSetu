import os
import joblib
import pandas as pd
from sklearn.linear_model import Ridge
from ml.training.targets import soil_target

MODEL_PATH = "models/soil.pkl"


def train(df):
    # Soil-only features
    soil_features = [
        c for c in df.columns
        if c.startswith("soil")
    ]

    assert len(soil_features) > 0, "❌ No soil moisture features found"

    X = df[soil_features]
    y = soil_target(df)

    # Combine & clean
    data = X.copy()
    data["target"] = y
    data = data.dropna()

    X_clean = data[soil_features]
    y_clean = data["target"]

    # Safety checks
    assert len(X_clean) > 100, (
        f"❌ Not enough soil samples: {len(X_clean)}"
    )

    model = Ridge(alpha=1.0)
    model.fit(X_clean, y_clean)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(
        f"✅ Soil model trained on {len(X_clean)} samples "
        f"with features {soil_features}"
    )


if __name__ == "__main__":
    df = pd.read_csv(
        "data_ingestion/data/features/features_weekly.csv",
        parse_dates=["week"]
    )

    train(df)
