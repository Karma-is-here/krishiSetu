from rainfall_loader import RainfallLoader

if __name__ == "__main__":
    loader = RainfallLoader("data/rainfall_2021_raw.csv")
    loader.save_clean("data/rainfall_2021_clean.csv")

    print("Rainfall data cleaned and saved successfully.")
