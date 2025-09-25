# %%
import sys
from src.Movie_Recommonder_System.components.monitering.logger import logging
from src.Movie_Recommonder_System.components.monitering.exception import CustomException
from src.Movie_Recommonder_System.components.data.preprocess import movies
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

# %%
ps = PorterStemmer()

def stem(text):
    try:
        y = []
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)
    except Exception as e:
        logging.error("Error in stemming function")
        raise CustomException(e, sys)

# %%

try:
    logging.info("Applying stemming to movie tags")
    movies['tags'] = movies['tags'].apply(stem)
    logging.info("Stemming applied successfully")
except Exception as e:
    logging.error("Error while applying stemming on 'tags' column")
    raise CustomException(e, sys)

# %%

try:
    logging.info("Vectorizing text data with CountVectorizer")
    vectors = CountVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_features=5000,
        max_df=0.85,
        min_df=2
    )

    vector = vectors.fit_transform(movies['tags']).toarray()
    logging.info(f"Text vectorization completed, shape: {vector.shape}")

except Exception as e:
    logging.error("Error in vectorization process")
    raise CustomException(e, sys)

# %%

try:
    logging.info("Calculating cosine similarity matrix")
    similarity = cosine_similarity(vector)
    logging.info("Cosine similarity matrix calculated successfully")
except Exception as e:
    logging.error("Error calculating cosine similarity")
    raise CustomException(e, sys)

# %%
# Train a model to recommend movies

def recommend_movies(movie):
    logging.info(f"Recommendation started for movie: {movie}")
    try:
        if movie not in movies['title'].values:
            raise ValueError(f"Movie '{movie}' not found in database")

        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        logging.info(f"Top 5 recommendations for '{movie}':")
        for i in movie_list:
            recommended = movies.iloc[i[0]].title
            print(recommended)
            logging.info(f"→ {recommended}")
            

    except Exception as e:
        logging.error("Error in Movie Recommender System")
        raise CustomException(e, sys)
