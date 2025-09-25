import os
import sys
import pandas as pd
from src.Movie_Recommonder_System.components.monitering.exception import CustomException
from src.Movie_Recommonder_System.components.monitering.logger import logging


# --------------------------Credits CSV ----------------------------------

def load_credits_csv (filename="tmdb_credits.csv"):

    try:
        logging.info("Reading credits CSV file started...")

        # Current directory (jaha raw.py hai)
        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

        # Project root tak jao (4 levels upar)
        PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", ".."))

        # CSV file ka path
        csv_path = os.path.join(PROJECT_ROOT, "csv_file", filename)

        logging.info(f"CSV absolute path generated: {csv_path}")

        # CSV read karo
        credits_file = pd.read_csv(csv_path)

        logging.info("Credits CSV file loaded successfully")
        return credits_file

    except Exception as e:
        logging.error("Error while reading Credits CSV file")
        raise CustomException(e, sys)


# --------------------------Movies CSV ----------------------------------
def load_movies_csv(filename="tmdb_movies.csv") :

    try :
        logging.info("Reading movies CSV file started...")
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir , ".." , ".." , ".." , ".."))
        csv_path = os.path.join(project_root , "csv_file" , filename)
        logging.info(f"CSV absolute path generated : {csv_path}")
        movie_csv = pd.read_csv(csv_path)
        logging.info("Movies CSV file loaded successfully")
        return movie_csv
    
    except Exception as e :
        logging.error("Error while reading movies CSV file")
        raise CustomException(e , sys)
    

# --------------------------Links CSV ----------------------------------
def merge_movie_and_credits(
    movies_raw="tmdb_movies.csv",
    credits_raw="tmdb_credits.csv",
    merged_filename="tmdb_5000_movies.csv"
):
    try:
        logging.info("Merging movies and credits CSV started...")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "..", "..", "..", ".."))
        csv_path = os.path.join(project_root, "csv_file")

        # Load raw CSVs
        movies_df = pd.read_csv(os.path.join(csv_path, movies_raw))
        credits_df = pd.read_csv(os.path.join(csv_path, credits_raw))

        # Merge on 'title'
        merged_df = movies_df.merge(credits_df, on="title")

        # Save merged CSV
        merged_file_path = os.path.join(csv_path, merged_filename)
        merged_df.to_csv(merged_file_path, index=False)

        logging.info(f"Merged CSV saved successfully as '{merged_filename}'")
        return merged_df

    except Exception as e:
        logging.error("Error while merging movies and credits CSV")
        raise CustomException(e, sys)