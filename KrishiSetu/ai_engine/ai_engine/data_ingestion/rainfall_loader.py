import pandas as pd


class RainfallLoader:
    """
    Loader for CHIRPS rainfall data exported from Google Earth Engine.
    Normalizes schema and prepares rainfall data for downstream processing.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_and_clean(self) -> pd.DataFrame:
        """
        Load raw rainfall CSV and normalize it to canonical schema:
        date, lat, lon, rainfall_mm
        """

        df = pd.read_csv(self.csv_path)

        # Normalize rainfall column name
        rainfall_cols = [
            "rainfall_mm",
            "precipitation",
            "precip",
            "precipitation_mm"
        ]

        for col in rainfall_cols:
            if col in df.columns:
                df = df.rename(columns={col: "rainfall_mm"})
                break
        else:
            raise ValueError("No rainfall / precipitation column found in CSV")

        # Robust date parsing (DD-MM-YYYY safe)
        df["date"] = pd.to_datetime(
            df["date"],
            dayfirst=True,
            errors="coerce"
        )

        df = df.dropna(subset=["date"])

        # Keep canonical columns
        df = df[["date", "lat", "lon", "rainfall_mm"]]

        # Physical sanity check (rainfall >= 0 mm)
        df = df[df["rainfall_mm"] >= 0.0]

        return df

    def save_clean(self, output_path: str):
        """
        Save cleaned rainfall data to CSV.
        """
        df = self.load_and_clean()
        df.to_csv(output_path, index=False)
