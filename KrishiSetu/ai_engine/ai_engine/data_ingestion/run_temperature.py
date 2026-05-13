from temperature_loader import ERA5Loader

if __name__ == "__main__":
    loader = ERA5Loader("data/temperature_2021_raw.csv")
    loader.save_clean("data/temperature_2021_clean.csv")

    print("ERA5 data cleaned and saved successfully.")