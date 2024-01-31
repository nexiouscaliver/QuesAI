#from langchain import HuggingFaceHub , LLMChain
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

hub_llm = HuggingFaceHub(
    repo_id = "google/flan-t5-large",
   model_kwargs={"temperature":0.6, "max_length":1000}  
)

prompt = PromptTemplate(
    input_variables = ['classs' , 'subject' , 'topic'],
    template = "Generate a subjective question from {subject} subject for {classs}th standard student about {topic} "
)

hub_chain = LLMChain(prompt=prompt , llm=hub_llm , verbose=True)
# que = hub_chain.invoke({"classs":'9' , "subject":'science' , "topic":'reproduction'})

def gen_ques(std:int , sub:str , topic:str):
    que = hub_chain.invoke({"classs":std , "subject":sub , "topic":topic})
    return (que['text'])
