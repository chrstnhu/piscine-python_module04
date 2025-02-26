# The goal of this exercise is to create a function displaying the proportion of participants
# who played a given sport, among the participants of a given gender.

import pandas as pd
import os

def proportion_by_sport(df, year, sport, gender):
        '''
        Takes a pandas.DataFrame as an argument and returns a float (proportion).
        '''
        # Find year and genre data
        year_genre_data = df.loc[(df['Year'] == year) & (df['Sex'] == gender)]


        # Find unique athletes in the year, genre data
        unique_athletes = year_genre_data.drop_duplicates(subset='Name')
        year_participants = unique_athletes.shape[0]
        # print(f"Number of participants: {year_participants} of year({year}) in olympics")


        # Find sport
        sport_data = year_genre_data.loc[year_genre_data['Sport'] == sport]
        # print(f"Find sport: {sport_data}")


        # Find unique participants in the sport
        unique_athletes = sport_data.drop_duplicates(subset='Name')
        participants_genre = unique_athletes.shape[0]
        # print(f"Number of participants: {participants_genre} of year({year}) in sport({sport})")

        if year_participants == 0 or participants_genre == 0:
            return 0.0
        else:
            print(f"In {year}, there were {year_participants} {gender} in olympics, {participants_genre} of them played {sport}")
            return float(participants_genre / year_participants)
