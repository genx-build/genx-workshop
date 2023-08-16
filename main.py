# wrapper class on prompt to reduce duplication
from pprint import pprint

from langchain.chains import LLMChain
# wrapper on LLM for Instructions
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from src.agents.linkedin_lookup_agent import lookup as lookup_agent
from src.external.linkedin import scrape_linkedin_profile

template = """""
    given the linkedin information {information} about the person. I want you to create:
    1- a short summery 
    2- two interesting fact about them
"""

if __name__ == "__main__":
    print("#########  start  ###########")
    tmp = PromptTemplate(input_variables=["information"], template=template)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=tmp)

    linkedin_profile_url = lookup_agent("mobin nikkhesal")
    print(linkedin_profile_url)
    profile = scrape_linkedin_profile(linkedin_profile_url)

    output = chain.run(information=profile)
    print(100 * "#")
    print(output)
