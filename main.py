from src.data_cleaning import load_and_clean_data
from src.feature_engineering import *

def main():
    # Load and clean data
    filepath = "data/marketing_campaign.csv"
    data = load_and_clean_data(filepath)

    # Feature engineering SO FAR
    data = add_shopper_length(data)   # shopper length feature
    data = add_age(data)              # Age of customers
    data = calculate_spent(data)      # Total spent from each customer over 2 years
    data = alone_or_partnered(data)   # Filter to determine if living by themself

    # Info on each column 
    print(data.info())
    print("Amount of data-points: ", len(data))

    # Results SO FAR
    print("Shopper Length Distribution:\n", data["Shopper_Length"].describe())
    print("Age of Customers", data["Age"].describe())
    print("Description of Total spent: ", data["Spent"].describe())

    print(data["Marital_Status"].value_counts())

if __name__ == "__main__":
    main()