# wrapper class on prompt to reduce duplication
from langchain.prompts import PromptTemplate
# wrapper on LLM for Instructions
from langchain.chat_models import ChatOpenAI  
from langchain.chains import LLMChain
import os

if __name__ == "__main__":
    simple_template = """
    what is {thing}?
    """
    tmp = PromptTemplate(input_variables=["thing"], template=simple_template)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=tmp)
    thing = "prompt"
    output = chain.run(thing)
    print(output)
