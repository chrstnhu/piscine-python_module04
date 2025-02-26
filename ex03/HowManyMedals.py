# The goal of this exercise is to implement a function that will return a dictionary of dictionaries 
# giving the number and types of medals for each year during which the participant won medals.

import pandas as pd
import os

def how_many_medals(df, name):
    '''
    - Takes a pandas.DataFrame and name
    - Returns a dictionary of dictionaries(number and types of medals for each year).
    '''
    
    # Find name
    name_data = df.loc[(df['Name'] == name)]

    # Filter out the years
    years = name_data['Year'].unique()

    # Number of medals of each year
    medals_count = {}
    for year in years:

        year_data = name_data[(name_data['Year'] == year)]

        gold = year_data[(year_data['Medal'] == 'Gold')].shape[0]
        silver = year_data[(year_data['Medal'] == 'Silver')].shape[0]
        bronze = year_data[(year_data['Medal'] == 'Bronze')].shape[0]

        # Store the medals count in the dictionary
        medals_count[year] = {'G': gold, 'S': silver, 'B': bronze}

    return medals_count

