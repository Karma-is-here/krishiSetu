import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from ml.training.targets import temperature_target

MODEL_PATH = "models/temperature.pkl"


def train(df):
    # Temperature-only features
    temp_features = [
        c for c in df.columns
        if c.startswith("temp")
    ]

    assert len(temp_features) > 0, "❌ No temperature features found"

    X = df[temp_features]
    y = temperature_target(df)

    # Combine & clean
    data = X.copy()
    data["target"] = y
    data = data.dropna()

    X_clean = data[temp_features]
    y_clean = data["target"]

    # Safety checks
    assert len(X_clean) > 100, (
        f"❌ Not enough temperature samples: {len(X_clean)}"
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_clean, y_clean)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(
        f"✅ Temperature model trained on {len(X_clean)} samples "
        f"with features {temp_features}"
    )


if __name__ == "__main__":
    df = pd.read_csv(
        "data_ingestion/data/features/features_weekly.csv",
        parse_dates=["week"]
    )

    train(df)
