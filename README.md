# Medium articles search system

## Modules
To run this program, the following packages need to be installed:
- streamlit
- langchain_community
- langchain
- sentence-transformers

To install these packages, run the following command: `pip install requrements.txt`


## Configuration
To configure the system, you can change the constant values in data_preparation.py, main.py, and ui.py. If you wish to modify a constant, you will need to change that constant in all mentioned files.

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"  
VECTOR_DB_PATH = "faiss_index"  
ARTICLES_CSV_PATH = "medium.csv"  
EXTRACTED_ARTICLES_DIRECTORY = "articles"

## Setup
The system consists of three main files:
-  data_preparation.py (optional)  
    This script extracts articles, chunks them, and creates a vector database. The program has already been run, so the data is prepared.
-  main.py  
For the console version of the program, run this file.
-  ui.py  
To run the UI version of the program, ensure the "streamlit" package is installed. Type the following command in the terminal within the project folder: `python3 -m streamlit run ui.py` or  `streamlit run ui.py`
