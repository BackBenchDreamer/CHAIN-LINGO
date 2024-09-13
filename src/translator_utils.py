import os
import json

from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.prompts import ChatPromptTemplate

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPEN_API_KEY = config_data["OPEN_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPEN_API_KEY

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=100)

def translate(input_language, output_language, input_text):
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
            ("human", "{input}")
        ]
    )
    
    chain = prompt | llm
    
    response = chain.invoke(
        {
            "input_language": input_language,
            "output_language": output_language,
            "input": input_text
        }
    )
    
    return response.content