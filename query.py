from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

query = "What is a neural network?"
docs = db.similarity_search(query)

print(len(docs))

# Print all the extracted Vectors from the above Query
for doc in docs:
  print("##---- Page ---##")
  print(doc.metadata['source'])
  print("##---- Content ---##")
  print(doc.page_content)