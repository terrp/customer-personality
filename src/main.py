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


# convert DT_Customer to datetime with pandas
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"], dayfirst=True)
dates = []
for i in data["Dt_Customer"]:
    i = i.date()
    dates.append(i)

# Print maximum and minimum to find oldest and newest
print("Longest time customer", min(dates))
print("Newest Customer", max(dates))

# Create list of the total days each shopper has been with us
days = []
day1 = max(dates)
for i in dates:
    delta = day1 - i
    days.append(delta)

# Create feature for the length of shoppers
data["Shopper_Length"] = days
data["Shopper_Length"] = pd.to_numeric(data["Shopper_Length"], errors="coerce")

print("All forms of education and their count:", data["Education"].value_counts(), "\n")
print("Total categories of Marital Status:", data["Marital_Status"].value_counts())