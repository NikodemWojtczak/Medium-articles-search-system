from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

hf = HuggingFacePipeline.from_model_id(
    # model_id="openai-community/gpt2",
    # model_id="microsoft/phi-1_5",
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
#
# template = """Question: {question}
#
# Answer: Let's think step by step."""
# prompt = PromptTemplate.from_template(template)
#
# chain = prompt | hf
#
# question = "What is CNN?"
#
# print(chain.invoke({"question": question}))

# Initialize a ConversationalRetrievalChain
query = ConversationalRetrievalChain.from_llm(
    llm=hf,
    retriever=db.as_retriever(),
    return_source_documents=True)

question = "What is CNN?"

print(query.invoke({"question": question, "chat_history": []}))