import matplotlib.pyplot as plt


def dataframe_plot(dim = 1, title = None):
    """
    Inputs: df - DataFrame, x - column name (x-axis), y - column name (y-axis), kind - Type of graph

    Display dataframe graph on a two different column
    
    Output: Return the ax for plotting
    """
    fig, ax = plt.subplots(dim)
   
    return fig, ax
    
    