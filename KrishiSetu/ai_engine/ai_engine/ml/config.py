WINDOW_SIZE = 8
STRIDE = 1

FEATURE_EXCLUDE = [
    "lat", "lon", "week",
    "ndvi_baseline", "soil_baseline", "temp_baseline"
]

TRAIN_YEARS = [2021, 2022, 2023, 2024]

MODEL_VERSION = "fusion_v1.0"
FEATURE_SCHEMA_VERSION = "features_v1.0"
