import pandas as pd

def main():
    print("Loading cleaned dataset...")
    df = pd.read_csv("cleaned_data/cleaned_data - Data_Dictionary_Cleaning_Log.csv")
    print(f"Cleaned dataset shape: {df.shape}")
    
    # Cancellation rate
    if 'is_canceled' in df.columns:
        cancel_rate = df['is_canceled'].mean() * 100
        print(f"Overall Cancellation Rate: {cancel_rate:.2f}%")
        
    # Lead time statistics
    if 'lead_time' in df.columns:
        print("\nLead Time Statistics:")
        print(df['lead_time'].describe())

if __name__ == "__main__":
    main()
