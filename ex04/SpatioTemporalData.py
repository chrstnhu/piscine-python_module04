# The goal of this exercise is to implement a class called SpatioTemporalData that takes
# a dataset (pandas.DataFrame) as argument in its constructor and implements two methods.

import pandas as pd
import os

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data
    
    def when(self, location):
        '''
        - Takes a location as an argument (City)
        - Returns a list containing the years where games were held in the given location,
        '''
        year = self.data[self.data['City'] == location]
        return list(year['Year'].astype(int).unique())

    def where(self, date):
        '''
        - Takes a date as an argument (Year)
        - Returns the location where the Olympics took place in the given year.
        '''
        city = self.data[self.data['Year'] == date]
        return city['City'].unique()


