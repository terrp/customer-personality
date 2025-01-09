import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Takes in scaled dataset and reduces to principle components
def reduce_dimensions(data):
    pca = PCA(n_components=3)
    pca.fit(data)
    PCA_ds = pd.DataFrame(pca.transform(data), columns=(["col1", "col2", "col3"]))
    print(PCA_ds.describe())
    return data

# Clustering the data, takes in PCA_ds
def cluster(data):
    
    return data