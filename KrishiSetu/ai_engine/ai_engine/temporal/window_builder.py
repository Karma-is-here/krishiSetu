# temporal/window_builder.py

def enforce_weekly_index(df):
    """
    Ensures:
    - sorted time
    - no duplicate weeks
    """

    df = df.sort_values(["lat", "lon", "week"])
    df = df.drop_duplicates(subset=["lat", "lon", "week"])

    return df
