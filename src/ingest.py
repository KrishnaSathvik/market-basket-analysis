import pandas as pd

def load_data(path):
    df = pd.read_csv(path, sep=';', low_memory=False)
    df = df.dropna(subset=["BillNo", "Itemname"])
    df["BillNo"] = df["BillNo"].astype(str)
    df["Itemname"] = df["Itemname"].str.strip()
    return df
