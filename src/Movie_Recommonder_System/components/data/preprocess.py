import pandas as pd
import sys
import os
# %%
import pandas as pd
from src.Movie_Recommonder_System.components.monitering.exception import CustomException
from src.Movie_Recommonder_System.components.monitering.logger import logging

from src.Movie_Recommonder_System.components.feture_engineering.feature_extrection import load_selected_movie_columns

movies = load_selected_movie_columns()

movies.head()

# %%
logging.info(f"Initial shape of dataset : {movies.shape}")

print (f"Shape of dataset : {movies.shape}") 


# %% [markdown]
# ### Handel Null and Duplicate value

# %%
logging.info("Checking for NaN and duplicate values...")
logging.info(f"No of NaN value : {movies.isna().sum() }")
logging.info(f"No of Duplicate value : {movies.duplicated().sum()}")

print (f"No of NaN value : {movies.isna().sum() }")
print (f"No of Duplicate value : {movies.duplicated().sum()}")  
movies.dropna(inplace=True)
print (f"Shape of dataset : {movies.shape}")

logging.info(f"Dropped NaN values. New shape: {movies.shape}")

# %% [markdown]
# ### Clean Genres

# %%
import ast 

def fetch_name (obj) :
    try :
        L = []
        for i in ast.literal_eval(obj) :
            L.append(i['name'])
        return L

    except Exception as e :
        logging.error(f"Error in fetch_name function : {e}")
        raise CustomException(e, sys)

# %%
# fetch_name(ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]'))

# %%
movies['genres'].iloc[0]

logging.info("Cleaning 'genres' column...")
movies['genres'] = movies['genres'].apply(fetch_name)

movies['genres'].iloc[1]

# %% [markdown]
# ###  keywords clean
# 
# same like genres here's we fetch name also so we can apply fetch_name function

# %%
logging.info("Cleaning 'keywords' column...")
movies['keywords'] = movies['keywords'].apply(fetch_name)
movies['keywords'].iloc[1]

movies.head(3)

# %% [markdown]
# ### change overview into a list
# 

# %%
logging.info("Cleaning 'overview' column...")
movies['overview']= movies['overview'].apply(lambda x: x.split())

movies.head(3)

# %% [markdown]
# ### Cast 
# 
# we only want top 3 actor name from the movie 

# %%
movies['cast'].iloc[0]

# it also same as genres and keywords but here's one extra logic we want top 3 actor name from the movie

# %%
fetch_actor = lambda x : [i['name'] for i in ast.literal_eval(x)][:3]

logging.info("Cleaning 'cast' column...")
movies['cast'] = movies['cast'].apply(fetch_actor)

movies['cast'].iloc[1]

# %%
Fetch_director = lambda x : [i['name'] for i in ast.literal_eval(x) if i['job'] == 'Director']

logging.info("🧼 Cleaning 'crew' column...")
movies['crew'] = movies['crew'].apply(Fetch_director)
movies['crew'].iloc[1]

# %%
movies.head(3)

# %% [markdown]
# ### Lowercase and merge words

# %%
logging.info("Lowercasing & removing spaces from all text columns...")

movies['genres'] = movies['genres'].apply(lambda x : [i.replace(" " , "").lower() for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x : [i.replace(" " , "").lower()for i in x])
movies['cast'] = movies['cast'].apply(lambda x : [i.replace (" ", "").lower()for i in x])
movies['crew'] = movies['crew'].apply(lambda x : [i.replace(" " , "").lower() for i in x])

movies.head(3)

# %%
logging.info(" Creating 'tags' column by merging all relevant features...")
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

movies.drop(columns = ['overview', 'genres', 'keywords', 'cast', 'crew'], inplace=True)

movies.head(3)

# %%
logging.info("'tags' column changed to string format...")

movies['tags'] = movies['tags'].apply(lambda x : " ".join(x))

movies['tags'].iloc[1]

# %%
logging.info("Preprocessing completed. Final DataFrame shape:")
logging.info(movies.shape)
print(movies.head(3))


