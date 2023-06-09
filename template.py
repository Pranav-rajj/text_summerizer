import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='%(levelname)s %(asctime)s | %(message)s:')

project_name = "Text_Summerizer"

list_of_files =[
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init.py",
    f"src/{project_name}/entity/_init.py",
    f"src/{project_name}/constants/_init.py",
    "config/config.yml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "" :
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for file: {filename}")

    if ( not os.path.exists(filepath) or ( os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating file: {filepath}")
    else:
        logging.info(f"file: {filepath} already exists")