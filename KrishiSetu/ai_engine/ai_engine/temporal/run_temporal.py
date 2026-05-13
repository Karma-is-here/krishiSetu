# temporal/run_temporal.py

import pandas as pd
from temporal.resampler import resample_to_weekly
from temporal.aligner import align_weekly_metrics
from temporal.window_builder import enforce_weekly_index
from temporal.window_validator import (
    validate_no_duplicates,
    validate_weekly_spacing
)

# ---------------- LOAD CLEAN DATA ---------------- #

rain = pd.read_csv("data_ingestion/data/clean/rainfall_clean.csv", parse_dates=["date"])
temp = pd.read_csv("data_ingestion/data/clean/temperature_clean.csv", parse_dates=["date"])
ndvi = pd.read_csv("data_ingestion/data/clean/ndvi_clean.csv", parse_dates=["date"])
soil = pd.read_csv("data_ingestion/data/clean/soil_clean.csv", parse_dates=["date"])

# ---------------- RESAMPLE ---------------- #

rain_w = resample_to_weekly(rain, "rainfall_mm", "sum")
temp_w = resample_to_weekly(temp, "temp_c", "max")
ndvi_w = resample_to_weekly(ndvi, "ndvi", "mean")
soil_w = resample_to_weekly(soil, "soil_moisture", "mean")

# ---------------- ALIGN ---------------- #

aligned = align_weekly_metrics({
    "rainfall_mm": rain_w,
    "temp_c": temp_w,
    "ndvi": ndvi_w,
    "soil_moisture": soil_w
})

# ---------------- VALIDATE ---------------- #

aligned = enforce_weekly_index(aligned)
validate_no_duplicates(aligned)
validate_weekly_spacing(aligned)

# ---------------- SAVE ---------------- #

aligned.to_csv("data_ingestion/data/aligned/aligned_weekly.csv", index=False)

print("✅ Temporal alignment complete")
