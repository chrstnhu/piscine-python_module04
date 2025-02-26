# The goal of this exercise is to write a function that returns a dictionary of dictionaries 
# giving the number and types of medals for each competition where a given country delegation earned medals.

import pandas as pd
import os
 
def how_many_medals_by_country(df, location):
    '''
    The function returns a dictionary of dictionaries giving the number and types of
    medals for each competition where the country delegation earned medals.
    
    The keys of the main dictionary are the Olympic games’ years. In each year’s dictionary, 
    the keys are ’G’, ’S’, ’B’ corresponding to the types of medals won.
    
    Duplicated medals per team games should be handled and not counted twice.
    
    Hint: You may find this list to be of some use.
    '''

    # Find location
    location_data = df.loc[(df['Team'] == location)]

    # Filter out the years
    years = location_data['Year'].unique()

    # Number of medals of each year
    medals_count = {}
    for year in years:

        year_data = location_data[(location_data['Year'] == year)]

        gold = year_data[(year_data['Medal'] == 'Gold')].shape[0]
        silver = year_data[(year_data['Medal'] == 'Silver')].shape[0]
        bronze = year_data[(year_data['Medal'] == 'Bronze')].shape[0]

        if gold == 0 and silver == 0 and bronze == 0:
            continue
        
        # Store the medals count in the dictionary
        medals_count[year] = {'G': gold, 'S': silver, 'B': bronze}
    
    # Sort the dictionary
    medals_count_keys = list(medals_count.keys())
    medals_count_keys.sort()

    sorted_medals_count = {i: medals_count[i] for i in medals_count_keys}

    return sorted_medals_count

