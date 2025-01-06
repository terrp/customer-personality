# Import Current Libraries
import numpy as np
import pandas as pd
import datetime
import matplotlib
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
from src.data_visualization import *

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
    data = add_is_parent(data)        # Determine if individual is parent

    # Drop features that are no longer relevant
    to_drop = ["Marital_Status", "Dt_Customer", "Z_CostContact", "Z_Revenue", "Year_Birth", "ID"]
    data = data.drop(to_drop, axis=1)

    '''
    # Describe all of the data so far
    with pd.option_context('display.max_columns', None):
        print(data.describe())
    '''

    data.to_csv("data/processed_data.csv", index=False)
            
    # Drop outliers in the data (noticed after plotting)
    data = data[(data["Age"] < 95) & (data["Income"] < 450000)]

    # Plot and show data
    relative_plot(data)
    

if __name__ == "__main__":
    main()