from langchain.document_loaders import TextLoader  #for textfiles
from langchain.text_splitter import CharacterTextSplitter #text splitter
from langchain.embeddings import HuggingFaceEmbeddings #for using HugginFace models
from langchain.vectorstores import FAISS  
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain_community.llms import HuggingFaceHub
from langchain.document_loaders import UnstructuredPDFLoader  #load pdf
from langchain.indexes import VectorstoreIndexCreator #vectorize db index with chromadb
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredURLLoader  #load urls into docoument-loader
from langchain.chains.question_answering import load_qa_chain
import csv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import HuggingFaceHub
import os

# cwd = os.getcwd()
cwd =os.path.abspath(os.path.join(os.getcwd(), os.pardir))
def load_pdf_to_db(pdfname=cwd+'\\datasets\\10-repo.pdf') -> FAISS:
    loader = PyPDFLoader(pdfname)
    pages = loader.load_and_split()
    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size = 1024,
        chunk_overlap = 64,
        #separators=['\n\n', '\n', '(?=>\. )', ' ', '']
    )
    docs = textsplitter.split_documents(pages)
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs , embeddings)
    return db

def load_run_query(query,db,k=2):
    llm=HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":1, "max_length":1000000})
    chain = load_qa_chain(llm,chain_type="stuff")

    opt_db = db.similarity_search(query)

    ans = chain.run(input_documents=opt_db,question=query)
    return ans


d = load_pdf_to_db()
a = load_qa_chain('What is reproduction?',d)
print(a)