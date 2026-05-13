import pandas as pd


class NDVILoader:
    """
    Loader for NDVI data exported from Google Earth Engine.
    Normalizes schema and prepares NDVI for downstream modeling.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_and_clean(self) -> pd.DataFrame:
        """
        Load raw NDVI CSV and normalize it to canonical schema:
        date, lat, lon, ndvi
        """

        df = pd.read_csv(self.csv_path)

        # Robust date parsing (DD-MM-YYYY safe)
        df["date"] = pd.to_datetime(
            df["date"],
            dayfirst=True,
            errors="coerce"
        )

        df = df.dropna(subset=["date"])

        # Keep canonical columns
        df = df[["date", "lat", "lon", "ndvi"]]

        # Physical sanity bounds for NDVI
        df = df[(df["ndvi"] >= -1.0) & (df["ndvi"] <= 1.0)]

        return df

    def save_clean(self, output_path: str):
        """
        Save cleaned NDVI data to CSV.
        """
        df = self.load_and_clean()
        df.to_csv(output_path, index=False)
