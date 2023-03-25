#importing the packages 


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


#def plot_regression(df):


#Reading the dataframe
data = pd.read_csv('iris.csv')
# Group the data by species
grouped_data = data.groupby('species')

# Loop through each species and perform linear regression
for x, group in grouped_data:
    slope, intercept, r_value, p_value, std_err = linregress(group['sepal_length_cm'], group['petal_length_cm'])
    #creat the plot 
    fig = plt.figure()
    plt.scatter(group['petal_length_cm'], group['sepal_length_cm'])
    plt.plot(group['petal_length_cm'], intercept + slope * group['petal_length_cm'], 'r')
    plt.title(x)
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()


    #save the plots 
    filename = x.lower().replace(' ', '_') + '.png'
    fig.savefig(filename)


#if __name__ == '__main__':
    # Load data into a pandas dataframe
    #df = pd.read_csv('iris_data.csv')

    # Call plot_regression function
    #plot_regression(df)
