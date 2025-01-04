import pandas as pd

# Create list of total days each shopper has been with us
def add_shopper_length(data):
    # Ensure Dt_Customer is in datetime format
    data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"], dayfirst=True)
    
    # Calculate the maximum date
    max_date = data["Dt_Customer"].max().date()
    
    # Calculate the difference in days for each customer
    data["Shopper_Length"] = data["Dt_Customer"].apply(lambda x: (max_date - x.date()).days)
    
    return data

# Create list of Age from Year_Birth
def add_age(data):
    data["Age"] = 2025-data["Year_Birth"]
    return data

