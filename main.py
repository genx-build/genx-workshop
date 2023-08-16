# wrapper class on prompt to reduce duplication
from pprint import pprint

from langchain.chains import LLMChain
# wrapper on LLM for Instructions
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from src.external.linkedin import scrape_linkedin_profile

template = """""
    given the linkedin information {information} about the person. I want you to create:
    1- a short summery 
    2- two interesting fact about them
"""

if __name__ == "__main__":
    tmp = PromptTemplate(input_variables=["information"], template=template)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=tmp)
    mp = "https://www.linkedin.com/in/mobin-nik-khesal/"
    ap = "https://www.linkedin.com/in/ali-khodadadi-b91b505b/"
    smj = "https://www.linkedin.com/in/s-muhammed-javad-feyzabadi-sani-8224ba162"
    pn = "https://www.linkedin.com/in/pouria-nikvand"
    profile = scrape_linkedin_profile(mp)

    output = chain.run(information=profile)
    print(100 * "#")
    print(output)
