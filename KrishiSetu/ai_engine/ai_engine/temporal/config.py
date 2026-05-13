# temporal/config.py

WEEK_FREQ = "W-MON"   # ISO week starting Monday

DATE_COL = "date"
LAT_COL = "lat"
LON_COL = "lon"

AGGREGATIONS = {
    "rainfall": "sum",
    "temperature": "max",
    "ndvi": "mean",
    "soil_moisture": "mean",
}

EVENT_AGG = "any"  # for IMD alerts
