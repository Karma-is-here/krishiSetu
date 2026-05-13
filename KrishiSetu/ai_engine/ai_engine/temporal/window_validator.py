# temporal/window_validator.py

import pandas as pd


def validate_no_duplicates(df):
    assert not df.duplicated(subset=["lat", "lon", "week"]).any(), \
        "Duplicate (lat, lon, week) found"


def validate_weekly_spacing(df):
    for _, g in df.groupby(["lat", "lon"]):
        diffs = g["week"].sort_values().diff().dropna()
        assert (diffs.dt.days == 7).all(), "Non-weekly spacing detected"


def validate_no_future_leakage(df, cutoff):
    assert df["week"].max() <= pd.to_datetime(cutoff), \
        "Future data leakage detected"
