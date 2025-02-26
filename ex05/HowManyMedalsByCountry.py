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
    # List of team sports
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing',
        'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
        'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
        'Rugby', 'Lacrosse', 'Polo']

    # Find team data
    location_data = df.loc[(df['Team'] == location)]
    # Filter out the years
    years = location_data['Year'].unique()
    # Dictionary to store the medals count
    medals_count = {}

    # Loop through the years
    for year in years:
        year_data = location_data[(location_data['Year'] == year)]
        medals_count[year] = {}
        # Check if team sport is already counted
        team_sports_counted = []

        # Loop through the sports
        for sport in sorted(year_data['Sport'].unique()):
            sport_data = year_data[(year_data['Sport'] == sport)]
            
            # If it's a team sport, count it only once
            if sport in team_sports and sport not in team_sports_counted:
                gold = sport_data[(sport_data['Medal'] == 'Gold')].shape[0]
                if gold > 0:
                    gold = 1
                silver = sport_data[(sport_data['Medal'] == 'Silver')].shape[0]
                if silver > 0:
                    silver = 1
                bronze = sport_data[(sport_data['Medal'] == 'Bronze')].shape[0]
                if bronze > 0:
                    bronze = 1

                if gold > 0 or silver > 0 or bronze > 0:
                    medals_count[year][sport] = {'G': gold, 'S': silver, 'B': bronze}
                    
                team_sports_counted.append(sport)
            else:
                gold = sport_data[(sport_data['Medal'] == 'Gold')].shape[0]
                silver = sport_data[(sport_data['Medal'] == 'Silver')].shape[0]
                bronze = sport_data[(sport_data['Medal'] == 'Bronze')].shape[0]

                if gold > 0 or silver > 0 or bronze > 0:
                    medals_count[year][sport] = {'G': gold, 'S': silver, 'B': bronze}

        # Remove the year if no medals were won
        if not medals_count[year]:
            del medals_count[year]

    # Sort the medals count by year
    medals_count_keys = sorted(medals_count.keys())

    # Dictionary to store the medals count
    dictionary_of_medals = {i: medals_count[i] for i in medals_count_keys}

    return dictionary_of_medals
