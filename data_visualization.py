def dataframe_plot(df, x, y, kind = 'line'):
    """
    Inputs: df - DataFrame, x - column name (x-axis), y - column name (y-axis), kind - Type of graph

    Display dataframe graph on a two different column
    
    Output: Return the ax for plotting
    """
    fig, ax = plt.subplots()
    ax = df.plot(x, y, kind = kind
           , title = '{} vs {}'.format(x, y), ax = ax);
    return fig, ax
    
    