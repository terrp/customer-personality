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
#import matplotlib.pyplot as plt, numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AgglomerativeClustering
#from matplotlib.colors import ListedColormap
from sklearn import metrics
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")
np.random.seed(42)


# Loading dataset to ensure no errors
data = pd.read_csv("data/marketing_campaign.csv", sep="\t")  # \t due to tab seperation
print("Number of datapoints: ", len(data))
print(data.head())