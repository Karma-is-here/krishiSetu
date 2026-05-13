# feature_engineering/rolling_features.py

import pandas as pd
from feature_engineering.config import GROUP_COLS, TIME_COL, ROLLING_WINDOWS


def add_rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(GROUP_COLS + [TIME_COL])

    for w in ROLLING_WINDOWS:
        df[f"rainfall_{w}w_sum"] = (
            df.groupby(GROUP_COLS)["rainfall_mm"]
              .rolling(w, min_periods=1)
              .sum()
              .reset_index(level=GROUP_COLS, drop=True)
        )

        df[f"temp_{w}w_mean"] = (
            df.groupby(GROUP_COLS)["temp_c"]
              .rolling(w, min_periods=1)
              .mean()
              .reset_index(level=GROUP_COLS, drop=True)
        )

        df[f"ndvi_{w}w_mean"] = (
            df.groupby(GROUP_COLS)["ndvi"]
              .rolling(w, min_periods=1)
              .mean()
              .reset_index(level=GROUP_COLS, drop=True)
        )

        df[f"soil_{w}w_mean"] = (
            df.groupby(GROUP_COLS)["soil_moisture"]
              .rolling(w, min_periods=1)
              .mean()
              .reset_index(level=GROUP_COLS, drop=True)
        )

    return df
