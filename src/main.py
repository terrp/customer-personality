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


# Loading dataset to ensure no errors
data = pd.read_csv("data/marketing_campaign.csv", sep="\t")  # \t due to tab seperation
#print("Number of datapoints: ", len(data))
#print(data.head())

#Information for each Column
print(data.info())
# Income only has 2216 values so the other 184 should be dropped
# Education, Marital Status, Dt_Customer are object types

data = data.dropna()
print("Amount of data-points: ", len(data))
# Outputs msg + 2216, confirms NA values dropped

# convert DT_Customer to datetime with pandas
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"], dayfirst=True)
dates = []
for i in data["Dt_Customer"]:
    i = i.date()
    dates.append(i)

# Print maximum and minimum to find oldest and newest
print("Longest time customer", min(dates))
print("Newest Customer", max(dates))