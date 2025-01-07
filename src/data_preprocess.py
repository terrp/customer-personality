from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def label_encode(data):
    # Change categorical variables to numeric
    categorical_index = (data.dtypes == 'object')
    objects = list(categorical_index[categorical_index].index)

    LE = LabelEncoder()

    # Loop through each column and assign number for category
    for i in objects:
        data[i] = LE.fit_transform(data[i])
    return data

