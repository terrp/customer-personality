from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd

def label_encode(data):
    # Change categorical variables to numeric
    categorical_index = (data.dtypes == 'object')
    objects = list(categorical_index[categorical_index].index)

    LE = LabelEncoder()

    # Loop through each column and assign number for category
    for i in objects:
        data[i] = LE.fit_transform(data[i])
    return data

def scale_data(data):
    # Copy the data 
    data_copy = data.copy()
    # Drop columns on deals accepted and complaints
    cols_del = ['AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1','AcceptedCmp2', 'Complain', 'Response']
    data_copy.drop(cols_del, axis = 1, inplace= True)

    # Scaling
    scaler = StandardScaler()
    scaler.fit(data_copy)
    scaled_ds = pd.DataFrame(scaler.transform(data_copy), columns= data_copy.columns)

    return scaled_ds