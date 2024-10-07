"""
This program looks for the best fitted articles based on user provided query.
Ir returns a specific number of the best matching results.


Requirements:
- A pre-built FAISS vector database: This database should contain the embeddings of articles previously indexed using
  the same embedding model specified in this script. The location of this database is defined by the VECTOR_DB_PATH constant.
- The embedding model: The name of the embedding model used for generating article embeddings
  is specified by the EMBEDDING_MODEL_NAME constant. It is crucial that this model matches the one used during
  the creation of the FAISS vector database to ensure compatibility and accuracy in the search results.
"""

from tools.articles_indexer import ArticlesIndexer
from dotenv import load_dotenv
import os 
load_dotenv()

# Load the vector database
articles_indexer = ArticlesIndexer(os.environ.get("EMBEDDING_MODEL_NAME")
)
db = articles_indexer.load_vector_db(os.environ.get("VECTOR_DB_PATH")
)

while(True):
    # User input for query and number of responses
    print("Type q to exit")
    query = input("Write here a query that you want to use to find articles: ")
    if query == "q":
        break
    number = input("How many responses do you want to get? ")
    try:
        num_responses = int(number)
        if num_responses <= 0:
            print("Please enter a positive integer.")
            exit()
    except ValueError:
        print("Please enter a valid integer.")
        exit()

    # Search for best fitted articles
    docs = db.similarity_search(query, k=num_responses)

    # Display the results
    for doc in docs:
        print("\n##---- Article path ---##\n")
        print(doc.metadata['source'])  # Path to the article
        print("\n##----   Content    ---##\n")
        print(doc.page_content)  # Article content
        print("\n-------------------------------------------------------------------------------------------------------\n")
