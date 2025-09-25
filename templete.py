import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "Movie_Recommonder_System"

list_of_file = {
    f"src/{project_name}/__init__.py" , 
    f"src/{project_name}/components/__init__.py"  , 
    f"src/{project_name}/components/data/__init__.py" ,  
    f"src/{project_name}/components/data/raw_data.py" ,  
    f"src/{project_name}/components/data/training_data.py" ,  
    f"src/{project_name}/components/data/testing_data.py" ,
    f"src/{project_name}/components/data/preprocess.py" ,
    f"src/{project_name}/components/feture_engineering/__init__.py" ,
    f"src/{project_name}/components/feture_engineering/vectorizetion.py" ,
    f"src/{project_name}/components/feture_engineering/feature_extrection.py" ,
    f"src/{project_name}/components/model/__init__.py" ,
    f"src/{project_name}/components/model/train.py" ,
    f"src/{project_name}/components/model/model.pkl" ,
    f"src/{project_name}/components/model/evaluation.py" ,
    f"src/{project_name}/components/web_app/__init__.py" ,
    f"src/{project_name}/components/web_app/app.py" ,
    f"src/{project_name}/components/monitering/__init__.py",
    f"src/{project_name}/components/monitering/logger.py" ,
    f"src/{project_name}/components/monitering/exception.py" ,
    f"src/{project_name}/components/web_app/dashbord.py" ,
    f"src/{project_name}/components/utills/__init__.py" ,
    f"src/{project_name}/components/utills/helper.py" ,
    f"src/{project_name}/tests/__init__.py" ,
    "Dockerfile" ,
    "requirement.txt" , 
    "main.py"  , 
    'csv_file/tmdb_credits.csv' , 
    'csv_file/tmdb_movies.csv'
    }

for files in list_of_file :
    file_path = Path(files)
    file_dir , file_name = os.path.split(files)

    if file_dir != "" : 
        os.makedirs(file_dir ,exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for the file : {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)== 0) :
        with open (file_path , 'w') as f :
            pass 
        logging.info(f"Creating Empty file , {file_path}")

    else :
        logging.info(f"File already exist {file_path}")