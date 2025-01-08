import pandas as pd
from sklearn.decomposition import PCA

# Takes in scaled dataset and reduces to primary components
def reduce_dimensions(data):
    pca = PCA(n_components=3)
    pca.fit(data)
    PCA_ds = pd.DataFrame(pca.transform(data), columns=(["col1", "col2", "col3"]))
    print(PCA_ds.describe())
    return data