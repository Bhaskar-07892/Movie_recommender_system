import pandas as pd
import sys
import os
from src.Movie_Recommonder_System.components.monitering.exception import CustomException
from src.Movie_Recommonder_System.components.monitering.logger import logging
from src.Movie_Recommonder_System.components.data.raw_data import merge_movie_and_credits


"""
columns to use : 
    'genres', 'id' , 'keywords',  'overview', 'title', 'cast', 'crew'
"""

def load_selected_movie_columns():
    try : 
        logging.info(f"Loading selected columns from merged movie and credits dataset")

        movies_df = merge_movie_and_credits()
        selected_column = ['genres', 'id' , 'keywords',  'overview', 'title', 'cast', 'crew']
        movies = movies_df[selected_column]
        logging.info(f"Selected columns loaded successfully from merged movie and credits dataset")
        return movies
    
    except Exception as e :
        logging.error("Error while loading selected coloumn from merged movie and credits dataset")
        raise CustomException(e , sys)


def save_data_to_csv(dataframe , filename="selected_movie_data.csv") :
    try :
        logging.info("Saving selected movie data to csv file started...")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir , ".." , ".." , ".." , ".."))
        csv_path = os.path.join(project_root , "csv_file" , filename)
        dataframe.to_csv(csv_path , index=False)

        logging.info(f"Selected movie data saved to csv file successfully at path : {csv_path}")

    except Exception as e :
        logging.error("Error while saving selected movie data to csv file")
        raise CustomException(e , sys)