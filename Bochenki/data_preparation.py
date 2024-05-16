"""
This program preprocesses data to be used in articles search system.
It extracts articles from medium.csv file then chunks articles and creates FAISS vector database of embedded chunks.

Note:
    If you want to change any constants please do it in ui.py and main.py file to make the system work properly
    This script takes about 20-25 minutes to run.
"""

from tools.articles_indexer import ArticlesIndexer
from tools.articles_extractor import ArticlesExtractor

# Configuration constants
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"  # Name of the model from Hugging face used for generating embeddings.
VECTOR_DB_PATH = "faiss_index"  # Path to save the FAISS vector database.
# ARTICLES_CSV_PATH = "medium.csv"  # Path to the source CSV file with articles.
EXTRACTED_ARTICLES_DIRECTORY = "data"  # Directory to save extracted articles as text files.


# Extract articles
extractor = ArticlesExtractor()
# extractor.extract_articles_from_csv(csv_file_path=ARTICLES_CSV_PATH,
#                                     output_directory=EXTRACTED_ARTICLES_DIRECTORY)



# Load and chunk articles
indexer = ArticlesIndexer(embedding_model_name=EMBEDDING_MODEL_NAME)
split_articles = indexer.load_and_split_articles(directory_path=EXTRACTED_ARTICLES_DIRECTORY)

# Create and save FAISS vector database
indexer.create_and_save_vector_db(split_documents=split_articles,
                                  data_base_path=VECTOR_DB_PATH)
