"""
This program is a UI implementation of an article search system
To run this program make sure you have installed the "streamlit" package and type in the terminal with the project folder:

python3 -m streamlit run ui.py
or just
streamlit run ui.py

Requirements:
- A pre-built FAISS vector database: This database should contain the embeddings of articles previously indexed using
  the same embedding model specified in this script. The location of this database is defined by the VECTOR_DB_PATH constant.
- The embedding model: The name of the embedding model used for generating article embeddings
  is specified by the EMBEDDING_MODEL_NAME constant.It is crucial that this model matches the one used during
  the creation of the FAISS vector database to ensure compatibility and accuracy in the search results.
"""

import streamlit as st
from tools.articles_indexer import ArticlesIndexer

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"  # Name of the model from Hugging face used for generating embeddings.
VECTOR_DB_PATH = "faiss_index"  # Path to save the FAISS vector database.


def query(quenstion, number_of_responses):
    articles_indexer = ArticlesIndexer(EMBEDDING_MODEL_NAME)
    db = articles_indexer.load_vector_db(VECTOR_DB_PATH)
    return db.similarity_search(quenstion,
                                k=number_of_responses)


st.title("Medium articles search engine")
st.header("Please enter your query below")
number_of_responses = st.number_input("How many responses do you want to get?",
                                      value=4,
                                      placeholder="Type a number...",
                                      step=1,
                                      min_value=1,
                                      max_value=10)
st.divider()

documents = []
if prompt := st.chat_input("Enter your query here: "):
    st.header(f"Your query: {prompt}")
    with st.spinner("Working on your query...."):
        documents = query(prompt, number_of_responses)

for doc in documents:
    st.subheader(doc.metadata['source'][9:-4])
    st.write(doc.page_content)
    with st.expander("See ful article"):
        with open(doc.metadata['source'], "r", encoding='utf-8') as file:
            st.write(file.read())
    st.divider()
