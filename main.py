# import pandas as pd
# from sentence_transformers import SentenceTransformer
# import faiss
# import numpy as np
#
# medium = pd.read_csv("medium.csv")
#
# # Assuming you have a list of articles where each article is a dict with 'title' and 'content'
#
# model = SentenceTransformer('all-MiniLM-L6-v2')
#
# def encode_text(text):
#     return model.encode(text)
#
# # Generate embeddings for titles and contents
# title_embeddings = np.array(medium['Title'].apply(encode_text).tolist())
# content_embeddings = np.array(medium['Text'].apply(encode_text).tolist())
#
# # Augment title and content embeddings by averaging
# augmented_embeddings = (title_embeddings + content_embeddings) / 2
#
# augmented_embeddings = content_embeddings
#
# # Indexing with FAISS
# dimension = augmented_embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(augmented_embeddings)
#
# def search(query, k=5):
#     query_embedding = model.encode(query)
#     _, indices = index.search(np.array([query_embedding]), k)
#     # Use .iloc to access rows by position
#     return medium.iloc[indices[0]]
#
#
# # Example search
# query = "AI in healthcare"
# results = search(query)
# print(results)
#


# CSV
#
# from langchain_community.document_loaders import DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import CSVLoader
#
# loader = CSVLoader(file_path='medium.csv', encoding='utf-8')
# documents = loader.load()
#
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
# )
#
# split_documents = text_splitter.split_documents(documents=documents)
# print(f"Split into {len(split_documents)} Documents...")
#
#
#
# from langchain_community.embeddings import HuggingFaceEmbeddings
#
# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#
# db = FAISS.from_documents(split_documents, embeddings)
# # Save the FAISS DB locally
# db.save_local("faiss_index")
#
#
#


from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = DirectoryLoader('articles')

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
)

split_documents = text_splitter.split_documents(documents=documents)
print(f"Split into {len(split_documents)} Documents...")

# Initialize embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create FAISS index from the split documents
db = FAISS.from_documents(split_documents, embeddings)

# Save the FAISS DB locally
db.save_local("faiss_index_from_txt")

