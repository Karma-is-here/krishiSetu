import pandas as pd


class ERA5Loader:
    """
    Loader for ERA5 temperature data exported from Google Earth Engine.
    Normalizes schema and prepares temperature for downstream modeling.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_and_clean(self) -> pd.DataFrame:
        """
        Load raw ERA5 CSV and normalize it to canonical schema:
        date, lat, lon, temperature_c
        """

        df = pd.read_csv(self.csv_path)

        # Convert date (DD-MM-YYYY safe)
        df["date"] = pd.to_datetime(
            df["date"],
            dayfirst=True,
            errors="coerce"
        )

        df = df.dropna(subset=["date"])

        # Keep canonical columns
        df = df[["date", "lat", "lon", "temp_c"]]

        # Physical sanity bounds (°C)
        df = df[
            (df["temp_c"] >= -80.0) &
            (df["temp_c"] <= 60.0)
        ]

        return df

    def save_clean(self, output_path: str):
        """
        Save cleaned temperature data to CSV.
        """
        df = self.load_and_clean()
        df.to_csv(output_path, index=False)
