import re

from googlesearch import search
from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, StrictStr
from src.logger_handler import LoggerHandler
from duckduckgo_search import DDGS

handler = LoggerHandler()


def _extract_profile_name(linkedin_urls: list[str]) -> str:
    pattern = r"linkedin\.com/in/([^/]+)"
    for url in linkedin_urls:
        match = re.search(pattern, url)
        if match:
            return url
        continue
    return ""


def _get_linkedin_profile_url_google(query: str) -> str:
    result = search(f"what is linkedin profile of {query}", num_results=1, lang="en")
    return _extract_profile_name(list(result)[:3])


def _get_linkedin_profile_url_ddg(query: str) -> str:
    pattern = r"linkedin\.com/in/([^/]+)"
    with DDGS(timeout=20) as ddg:
        for r in ddg.text(f"what is linkedin profile of {query}"):
            match = re.search(pattern, r["href"])
            if match:
                return r["href"]
            continue
        return ""


class _SearchQuery(BaseModel):
    query: StrictStr


def lookup(name: str) -> str:
    template = """given full name {query}, I want you to get me the link of their linkedin profile page
    your answer must contain only url!!!."""

    tools_for_agent = [
        Tool(
            name="crawl google 4 linkedin profile page",
            func=_get_linkedin_profile_url_ddg,
            description="useful when you want get linkedin profile",
            args_schema=_SearchQuery,
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=ChatOpenAI(temperature=0),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(input_variables=["query"], template=template)
    return agent.run(prompt_template.format_prompt(query=name), callbacks=[handler])
