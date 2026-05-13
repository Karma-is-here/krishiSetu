# temporal/resampler.py

import pandas as pd
from temporal.config import WEEK_FREQ, DATE_COL, LAT_COL, LON_COL


def resample_to_weekly(
    df: pd.DataFrame,
    value_col: str,
    agg: str
) -> pd.DataFrame:
    """
    Input:
      date, lat, lon, value
    Output:
      lat, lon, week, value
    """

    df = df.copy()
    df[DATE_COL] = pd.to_datetime(df[DATE_COL])

    df = (
        df
        .set_index(DATE_COL)
        .groupby([LAT_COL, LON_COL])
        .resample(WEEK_FREQ)[value_col]
        .agg(agg)
        .reset_index()
        .rename(columns={DATE_COL: "week"})
    )

    return df
