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
    print('Number of observation:', len(data.index))
    
    if True in data.duplicated().value_counts().keys():
        print('Duplicates detected')
        display(data[data.duplicated(keep= False)])
    
    results = data.isna().any()
    if True in results.values:
        print('N/A detected')
        print('Columns with NaN: ', list(results[results.values == True].index))
        
def look_columns(data, columns):
    """
    Input: DataFrame Series
    
    Output: None
    Display: Column unique values and notice any strange data points.
    
    """
    if type(columns) != list:
        columns = [columns]
    display(data[columns].head())
    for column in columns:
        if(len(data[column].unique()) == len(data)):
            print('{} has all unique observations. '.format(column))
        else:
            print('{} has {}/{} unique observations. '.format(column, len(data[column].unique()), len(data)))
        display(data[columns][data[column].duplicated(keep = False)].sort_values(column))
