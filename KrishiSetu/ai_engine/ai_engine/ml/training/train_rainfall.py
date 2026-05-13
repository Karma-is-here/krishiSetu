import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from ml.training.targets import rainfall_target


MODEL_PATH = "models/rainfall.pkl"

def train(df):
    # Rainfall-only features (CRITICAL)
    rainfall_features = [
        c for c in df.columns
        if c.startswith("rainfall")
    ]

    assert len(rainfall_features) > 0, "❌ No rainfall features found"

    X = df[rainfall_features]
    y = rainfall_target(df)

    # Combine & clean
    data = X.copy()
    data["target"] = y
    data = data.dropna()

    X_clean = data[rainfall_features]
    y_clean = data["target"]

    # Safety checks
    assert len(X_clean) > 100, (
        f"❌ Not enough clean rainfall samples: {len(X_clean)}"
    )
    assert y_clean.nunique() > 1, (
        "❌ Rainfall target collapsed to a single class"
    )

    # Train classifier
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    )
    model.fit(X_clean, y_clean)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(
        f"✅ Rainfall model trained on {len(X_clean)} samples "
        f"with features {rainfall_features}"
    )




# 🔑 EXECUTION ENTRY POINT (CRITICAL)
if __name__ == "__main__":
    df = pd.read_csv(
        "data_ingestion/data/features/features_weekly.csv",
        parse_dates=["week"]
    )

    train(df)
