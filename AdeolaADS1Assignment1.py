# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset in to a DataFrame
gdp_scan_country = pd.read_csv('GDP_data_2015_to_2019_Finland_Norway_Sweden.csv', index_col=0)

# Creating the list of year to be plotted
gdp_year = ['2015', '2016', '2017', '2018', '2019']

# This function is used to plot a line graph of multiple lines

def plot_gdp_lines(gdp_scan_country, x_col, y_cols, title, x_label, y_label):
    """
    Plots a line graph given a dataframe, x_col, y_cols, title, x label, and y label.

    Args:
    df (pandas.DataFrame): The dataframe containing the data to plot.
    x_col (str): The name of the column containing the x-axis data.
    y_cols (list of str): The names of the columns containing the y-axis data.
    title (str): The line plot title.
    x_label (str): The line plot label for the horizontal-axis.
    y_label (str): The line plot label for the vertical-axis.
    """
    plt.figure(figsize=(10, 6))
    for col in y_cols:
        plt.plot(gdp_year, gdp_scan_country[col], label=col)
        
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(loc='upper left')
    plt.show()

plot_gdp_lines(gdp_scan_country, 'year', list(gdp_scan_country.columns), 'GDP of Finland Norway & Sweden (2015-2019)', 'Year', 'GDP (in billions of USD)')

# This function is used to plot a stacked bar chart
def plot_gdp_stacked_bar(gdp_scan_country):
    """
    Plots a stacked bar chart of GDP for Nordic countries in the selected year.

    Args:
    gdp_scan_country (pandas.DataFrame): The dataframe containing the data to plot.
    
    none
    """
    gdp_scan_country.plot(kind='bar', stacked=True)
    plt.xlabel('Year')
    plt.ylabel('GDP (in billion US dollars)')
    plt.title(f'Comparison of GDPs for 3 Scandinavian Countries')
    plt.legend(loc='best')

    plt.show()

plot_gdp_stacked_bar(gdp_scan_country)

# This function is used to plot a pie chart
def plot_pie_chart(year, countries):
    """
    Plots a pie chart of the GDPs of different countries for a particular year.

    Parameters:
    gdp_scan_country (pd.DataFrame): A pandas dataframe with columns as years and rows as countries
    year (int): The year for which the GDPs are to be compared
    countries: The columns that contains the  scandinavian countries

    Returns:
    None
    """   
    gdp_scan = gdp_scan_country.loc[2019]
    
# Plotting a pie chart of the GDP of the Scandinavian countries  
    plt.figure()
    
    plt.pie(gdp_scan, labels=gdp_scan.index, autopct='%2.1f%%')
    plt.title(f'GDPs of 3 Scandinavian Countries(Finland,Norway & Sweden)')
    plt.legend(loc='best')
    plt.show()


plot_pie_chart('year', gdp_scan_country.columns)
    