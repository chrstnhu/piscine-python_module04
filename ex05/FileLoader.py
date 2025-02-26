# The goal of this exercise is to create a Fileloader class containing a load and a display method.

import pandas as pd
import os

class FileLoader:
    def load(self, path):
        # Check if the file exists and if the path is a valid string
        if not isinstance(path, str) or not os.path.exists(path):
            print("Invalid file path or file does not exist.")
            return None
        
        try:
            # Load the dataset into a pandas DataFrame
            df = pd.read_csv(path)
            # Get the shape of the dataframe (rows, columns)
            print(f"Loading dataset of dimensions: {df.shape[0]} x {df.shape[1]}")
            # Return the loaded dataframe
            return df
        except pd.errors.ParserError as e:
            print(f"Error parsing the file: {e}")
            return None

    def display(self, df, n):
        '''
        Takes a pandas.DataFrame as an argument and size(n) and displays
        '''
        # Check if the input is a pandas DataFrame
        if not isinstance(df, pd.DataFrame):
            print("Invalid input. Please provide a pandas DataFrame.")
            return None
        
        # Display the first n rows of the dataframe
        print(df.head(n))
        return df

