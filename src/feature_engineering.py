import pandas as pd
import numpy as np

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

# Total Spending for each Customer
def calculate_spent(data):
    data["Spent"] = data["Wines"] + data["Fruits"]+ data["Meat"] + data["Fish"] + data["Sweets"] + data["Gold"]
    return data

# To determine if individual is providing for more than themselves
def alone_or_partnered(data):
    data["Living_With"] = data["Marital_Status"].replace({
        "Married":"Partner",
        "Together":"Partner",
        "Single":"Alone",
        "Divorced":"Alone",
        "Widow":"Alone",
        "Alone":"Alone",
        "Absurd":"Alone",
        "YOLO":"Alone"
        })
    return data

# Children Count to make Family size feature
def children_count(data):
    data["Children_Count"] = data["Kidhome"] + data["Teenhome"]
    return data

def family_size(data):
    data["Family_Size"] = data["Living_With"].replace({"Partner": 2, "Alone": 1}) + data["Children_Count"]
    return data

# Group Education into three categories
def add_education(data):
    data["Education"] = data["Education"].replace({
        "Graduation": "Graduate",
        "PhD": "Higher_Education",
        "Master": "Higher_Education",
        "2n Cycle": "Undergraduate",
        "Basic": "Undergraduate"
    })
    return data

def add_is_parent(data):
    data["Is_Parent"] = np.where(data.Children_Count > 0, 1, 0)
    return data