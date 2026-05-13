# feature_engineering/trends.py

import pandas as pd
from feature_engineering.config import GROUP_COLS, TIME_COL


def add_trend_features(df: pd.DataFrame, window: int = 4) -> pd.DataFrame:
    df = df.sort_values(GROUP_COLS + [TIME_COL])

    df["ndvi_trend"] = (
        df.groupby(GROUP_COLS)["ndvi"]
          .diff(window)
    )

    df["rainfall_trend"] = (
        df.groupby(GROUP_COLS)["rainfall_mm"]
          .diff(window)
    )

    return df
