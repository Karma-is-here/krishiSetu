import pandas as pd


class SMAPLoader:
    """
    Loader for SMAP soil moisture data exported from Google Earth Engine.
    Normalizes schema and prepares soil moisture for downstream modeling.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_and_clean(self) -> pd.DataFrame:
        df = pd.read_csv(self.csv_path)

        df["date"] = pd.to_datetime(
            df["date"],
            dayfirst=True,
            errors="coerce"
        )

        df = df.dropna(subset=["date"])

        df = df[["date", "lat", "lon", "sm_surface"]]
        df = df.rename(columns={"sm_surface": "soil_moisture"})

        df = df[(df["soil_moisture"] >= 0.0) & (df["soil_moisture"] <= 0.7)]

        return df


    def save_clean(self, output_path: str):
        """
        Save cleaned soil moisture data to CSV.
        """
        df = self.load_and_clean()
        df.to_csv(output_path, index=False)
