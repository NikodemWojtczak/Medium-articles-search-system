"""
This program preprocesses data to be used in articles search system.
It extracts articles from medium.csv file then chunks articles and creates FAISS vector database of embedded chunks.

Note:
    If you want to change any constants please do it in ui.py and main.py file to make the system work properly
    This script takes about 20-25 minutes to run.
"""

from tools.articles_indexer import ArticlesIndexer
from tools.articles_extractor import ArticlesExtractor
from dotenv import load_dotenv
import os
load_dotenv()


# Extract articles
extractor = ArticlesExtractor()
extractor.extract_articles_from_csv(csv_file_path=os.environ.get("ARTICLES_CSV_PATH")
,
                                    output_directory=os.environ.get("EXTRACTED_ARTICLES_DIRECTORY")
)



# Load and chunk articles
indexer = ArticlesIndexer(embedding_model_name=os.environ.get("EMBEDDING_MODEL_NAME")
)
split_articles = indexer.load_and_split_articles(directory_path=os.environ.get("EXTRACTED_ARTICLES_DIRECTORY")
)

# Create and save FAISS vector database
indexer.create_and_save_vector_db(split_documents=split_articles,
                                  data_base_path=os.environ.get("VECTOR_DB_PATH")
)
