# The goal of this exercise is to introduce you to plotting methods 
# using different libraries like Pandas, Matplotlib, Seaborn or Scipy.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import spicy as sp

import os
 
class MyPlotLib :
    def histogram(self, data, features): 
        '''
        Plots one histogram for each numerical feature in the list,
        '''
        fig, axes = plt.subplots(1, 2)

        data.hist(column=features[1], bins=30, ax=axes[0])
        data.hist(column=features[0], bins=30, ax=axes[1])
    
        plt.show()

    def density(self, data, features): 
        '''
        Plots the density curve of each numerical feature in the list,
        '''
        sns.kdeplot(data[features])
        plt.show()
    
    # def pair_plot(self, data, features): 
    #     '''
    #     Plots a matrix of subplots (also called scatter plot matrix). 
    #     On each subplot shows a scatter plot of one numerical variable against
    #     another one. The main diagonal of this matrix shows simple histograms.
    #     '''

    # def box_plot(self, data, features): 
    #     '''
    #     Displays a box plot for each numerical variable in the dataset.
    #     '''