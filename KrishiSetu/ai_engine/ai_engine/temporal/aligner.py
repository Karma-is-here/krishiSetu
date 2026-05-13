# temporal/aligner.py

import pandas as pd
from functools import reduce
from temporal.config import LAT_COL, LON_COL


def align_weekly_metrics(weekly_tables: dict) -> pd.DataFrame:
    """
    weekly_tables = {
        "rainfall_mm": df,
        "temp_c": df,
        ...
    }
    """

    dfs = []
    for name, df in weekly_tables.items():
        df = df.copy()
        value_col = [c for c in df.columns if c not in ["lat", "lon", "week"]][0]
        df = df.rename(columns={value_col: name})
        dfs.append(df)

    aligned = reduce(
        lambda left, right: pd.merge(
            left, right,
            on=[LAT_COL, LON_COL, "week"],
            how="outer"
        ),
        dfs
    )

    return aligned
