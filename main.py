# Import Current Libraries
import numpy as np
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")
np.random.seed(55)
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
    data = children_count(data)       # Count amount of children per household
    data = family_size(data)          # Count of all members in house
    data = add_education(data)        # Filter Education into 3 groups

    # Info on each column 
    print(data.info())
    print("Amount of data-points: ", len(data))

    ''' 
    #Results SO FAR
    print("Shopper Length Distribution:\n", data["Shopper_Length"].describe())
    print("Age of Customers", data["Age"].describe())
    print("Description of Total spent: ", data["Spent"].describe())
    print("Counts of individuals living situation", data["Living_With"].value_counts())
    print("Counts of houses with sets of children", data["Children_Count"].value_counts())
    print("Counts of houses with sets of children", data["Family_Size"].value_counts())
    print("Counts of each level of Education: ", data["Education"].value_counts())
    '''

    # Drop features that are no longer relevant
    to_drop = ["Marital_Status", "Dt_Customer", "Z_CostContact", "Z_Revenue", "Year_Birth", "ID"]
    data = data.drop(to_drop, axis=1)

    print(data.describe())
    

if __name__ == "__main__":
    main()