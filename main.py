from src.data_cleaning import load_and_clean_data
from src.feature_engineering import add_shopper_length

def main():
    # Load and clean data
    filepath = "data/marketing_campaign.csv"
    data = load_and_clean_data(filepath)

    # Feature engineering SO FAR
    data = add_shopper_length(data)   # shopper length feature

    # Info on each column 
    print(data.info())
    print("Amount of data-points: ", len(data))

    # Results SO FAR
    print("Shopper Length Distribution:\n", data["Shopper_Length"].describe())

if __name__ == "__main__":
    main()