from soil_moisture_loader import SMAPLoader

if __name__ == "__main__":
    loader = SMAPLoader("data/soil_2021_raw.csv")
    loader.save_clean("data/soil_2021_clean.csv")

    print("SMAP data cleaned and saved successfully.")