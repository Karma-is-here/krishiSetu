from ndvi_loader import NDVILoader

if __name__ == "__main__":
    loader = NDVILoader("data/ndvi_2021_raw.csv")
    loader.save_clean("data/ndvi_2021_clean.csv")

    print("NDVI data cleaned and saved successfully.")
