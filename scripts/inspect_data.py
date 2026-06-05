import pandas as pd

def main():
    print("Loading raw dataset...")
    df = pd.read_csv("Raw_DataSet/Capstone_HotelBooking.csv")
    print(f"Dataset shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumns and Data Types:")
    print(df.info())

if __name__ == "__main__":
    main()
