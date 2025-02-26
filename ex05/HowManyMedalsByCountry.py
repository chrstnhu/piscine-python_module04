# The goal of this exercise is to write a function that returns a dictionary of dictionaries 
# giving the number and types of medals for each competition where a given country delegation earned medals.

import pandas as pd
import os
 
def how_many_medals_by_country(df, location):
    '''
    The function returns a dictionary of dictionaries giving the number and types of
    medals for each competition where the country delegation earned medals.
    
    The keys of the main dictionary are the Olympic games' years. In each year's dictionary, 
    the keys are 'G', 'S', 'B' corresponding to the types of medals won.
    
    Duplicated medals per team games should be handled and not counted twice.
    
    Hint: You may find this list to be of some use.
    '''
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing',
        'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
        'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
        'Rugby', 'Lacrosse', 'Polo']

    # Find location
    location_data = df.loc[(df['Team'] == location)]

    # Filter out the years
    years = location_data['Year'].unique()

    # Number of medals of each year
    medals_count = {}
    for year in years:

        year_data = location_data[(location_data['Year'] == year)]

        medals_count[year] = {}
        
        for sport in sorted(year_data['Sport'].unique()):
            sport_data = year_data[(year_data['Sport'] == sport)]

            gold = year_data[(year_data['Medal'] == 'Gold')].shape[0]
            silver = year_data[(year_data['Medal'] == 'Silver')].shape[0]
            bronze = year_data[(year_data['Medal'] == 'Bronze')].shape[0]

            if gold > 0 or silver > 0 or bronze > 0:
                medals_count[year][sport] = {'G': gold, 'S': silver, 'B': bronze}
            
        
        if not medals_count[year]:
            del medals_count[year]
    
    # Sort the dictionary
    medals_count_keys = sorted(medals_count.keys())

    sorted_medals_count = {i: medals_count[i] for i in medals_count_keys}

    return sorted_medals_count

