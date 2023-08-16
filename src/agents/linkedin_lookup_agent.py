from googlesearch import search
from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, StrictStr


def _get_linkedin_profile(query: str) -> str:
    result = search(f"what is linkedin profile of {query}", num_results=1, lang="en")
    return list(result)[0]


class _SearchQuery(BaseModel):
    query: StrictStr


def lookup(name: str) -> str:
    template = """given full name {query}, I want you to get me the link of their linkedin profile page
    your answer must contain only url!!!."""

    tools_for_agent = [
        Tool(
            name="crawl google 4 linkedin profile page",
            func=_get_linkedin_profile,
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
    return agent.run(prompt_template.format_prompt(query=name))
