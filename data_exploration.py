import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import scipy

def look_dataframe(data):
    """
    Input: dataframe
    
    Output: None
    Displays: first 5 rows, list column names, list row names,
            duplicates if any, null/nan if any
    
    Explore dataframe for information and give a quick overview of 
    potenital important information before prepping.
    
    """
    display(data.head())
    print('Column Names:', list(data.columns))
    print('Index Names:', list(data.index))
    
    if True in data.duplicated().value_counts().keys():
        print('Duplicates detected')
        display(data[data.duplicated(keep= False)])
    
    if True in data.isna().value_counts().keys():
        print('N/A detected')
        display(data.info())