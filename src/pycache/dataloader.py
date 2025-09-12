import pandas as pd
import os

def data_load(path):
    df = pd.read_csv(path)
    return df