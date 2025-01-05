import pandas as pd

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath, sep="\t")
    data = data.dropna()
    data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"], dayfirst=True)
    data = data.rename(columns={
        "MntWines": "Wines",
        "MntFruits":"Fruits",
        "MntMeatProducts":"Meat",
        "MntFishProducts":"Fish",
        "MntSweetProducts":"Sweets",
        "MntGoldProds":"Gold"})
    return data

