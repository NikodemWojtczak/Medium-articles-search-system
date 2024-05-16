from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


class ArticlesIndexer:
    """
    ArticlesIndexer is designed to index articles by converting them into embeddings using a specified
    transformer model from Hugging Face, and then storing these embeddings in a FAISS index for efficient
    similarity searches. It processes articles by loading them from a directory, splitting them into smaller
    chunks, generating embeddings for each chunk, and finally storing these embeddings in a vector database.

    Attributes:
        EMBEDDING_MODEL_NAME (str): The name of the pre-trained model from Hugging Face used for embedding the articles.
    """

    def __init__(self, embedding_model_name: str):
        """
        Initializes the ArticlesIndexer with a specific embedding model.

        Args:
            embedding_model_name (str): Name of the Hugging Face transformer model to use for embeddings.
        """
        self.EMBEDDING_MODEL_NAME = embedding_model_name

    def load_and_split_articles(self, directory_path: str) -> list:
        """
        Loads articles from a specified directory and splits them into smaller chunks based on the defined
        chunk size and overlap.

        Args:
            directory_path (str): The path to the directory containing text files with articles.

        Returns:
            list: A list of chunks.
        """
        # Load documents
        loader = DirectoryLoader(directory_path)
        documents = loader.load()

        # Chunk the documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                       chunk_overlap=50,
                                                       separators=["\n\n", "\n", " ", ""])
        split_documents = text_splitter.split_documents(documents=documents)

        return split_documents

    def create_and_save_vector_db(self, split_documents: list, data_base_path: str) -> object:
        """
        Creates a vector database (FAISS index) from the list of split documents by generating embeddings
        for each document chunk and then saving the database to the specified path.

        Args:
            split_documents (list): A list of split document chunks.
            data_base_path (str): The path where the vector database will be saved.

        Returns:
            object: The FAISS database object.
        """
        embeddings = HuggingFaceEmbeddings(model_name=self.EMBEDDING_MODEL_NAME)
        db = FAISS.from_documents(split_documents, embeddings)
        db.save_local(data_base_path)

        return db

    def load_vector_db(self, data_base_path: str) -> object:
        """
        Loads a previously created vector database (FAISS index) from the specified path.

        Args:
            data_base_path (str): The path to the saved FAISS vector database.

        Returns:
            object: The loaded FAISS database object, ready for queries.
        """
        embeddings = HuggingFaceEmbeddings(model_name=self.EMBEDDING_MODEL_NAME)
        db = FAISS.load_local(data_base_path, embeddings, allow_dangerous_deserialization=True)

        return db
