import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.head())
    

    # Create scatter plot

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    #plt.show()
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Create first line of best fit
    Year = df['Year']
    CSIRO = df['CSIRO Adjusted Sea Level']
    x = Year.values
    y = CSIRO.values
    fit1 = linregress(x, y)
    slope = fit1.slope
    intercept = fit1.intercept
    

    years_extended = np.arange(df['Year'].min(), 2051)

    predicted_sea_levels = slope * years_extended + intercept

    plt.plot(years_extended, predicted_sea_levels, color='red')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000] 
    x_filtered = df_filtered['Year'].values
    y_filtered = df_filtered['CSIRO Adjusted Sea Level'].values
    fit2 = linregress(x_filtered, y_filtered)
    slope_filtered = fit2.slope
    intercept_filtered = fit2.intercept

    years_extended_filtered = np.arange(df_filtered['Year'].min(), 2051)
    predicted_sea_levels_filtered = slope_filtered * years_extended_filtered + intercept_filtered
    plt.plot(years_extended_filtered, predicted_sea_levels_filtered, color='green', label='Best Fit Line (2000 - Most Recent)')


    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
  
   
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()