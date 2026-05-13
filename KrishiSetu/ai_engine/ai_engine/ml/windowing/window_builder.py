import numpy as np

def build_windows(df, feature_cols, window_size):
    X, meta = [], []
    df = df.sort_values(["lat", "lon", "week"])

    for (lat, lon), g in df.groupby(["lat", "lon"]):
        g = g.reset_index(drop=True)

        for i in range(len(g) - window_size + 1):
            w = g.iloc[i:i + window_size]
            if w[feature_cols].isna().mean().mean() > 0.4:
                continue

            X.append(w[feature_cols].values.astype("float32"))
            meta.append({
                "lat": lat,
                "lon": lon,
                "end_week": w["week"].iloc[-1]
            })

    return X, meta
