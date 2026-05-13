def vegetation_target(df):
    return (df["ndvi_anomaly"].shift(-2) < -0.15).astype(int)

def rainfall_target(df):
    return (df["rainfall_8w_sum"] < 20).astype(int)

def soil_target(df):
    return (df["soil_moisture_anomaly"] < -0.1).astype(int)

def temperature_target(df):
    return (df["temp_anomaly"] > 2.0).astype(int)
