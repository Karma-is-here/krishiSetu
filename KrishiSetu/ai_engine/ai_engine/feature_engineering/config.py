# feature_engineering/config.py

TRAIN_YEARS = [2021, 2022, 2023, 2024]

ROLLING_WINDOWS = [4, 8]   # weeks

BASELINE_METHOD = "mean"  # per-tile baseline

GROUP_COLS = ["lat", "lon"]
TIME_COL = "week"
