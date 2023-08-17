# wrapper class on prompt to reduce duplication
from pprint import pprint

from langchain.chains import LLMChain
# wrapper on LLM for Instructions
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from src.agents.linkedin_lookup_agent import lookup as lookup_agent
from src.external.linkedin import scrape_linkedin_profile
from src.output_parser import UserInfo, user_info_parser


def llm_engine(user_profile_name: str) -> UserInfo:
    template = """
        given the linkedin information {information} about the person. I want you to create:
        1- a paragraph summery 
        2- two interesting fact about them
        3- how many connection they have
        \n{format_instructions}
        """
    tmp = PromptTemplate(
        input_variables=["information"],
        template=template,
        partial_variables={
            "format_instructions": user_info_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=tmp)

    linkedin_profile_url = lookup_agent(user_profile_name)
    print(linkedin_profile_url)
    profile = scrape_linkedin_profile(linkedin_profile_url)

    output = chain.run(information=profile)
    print(100 * "#")
    return user_info_parser.parse(output)
