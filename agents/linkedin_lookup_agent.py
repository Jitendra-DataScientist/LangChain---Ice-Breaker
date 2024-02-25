from langchain import hub
# from langchain import PromptTemplate    # deprecated or about to be deprecated
# from langchain.prompts import PromptTemplate    # deprecated or about to be deprecated
from langchain_core.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI    # deprecated or about to be deprecated
# from langchain_community.chat_models import ChatOpenAI    # deprecated or about to be deprecated
from langchain_openai import ChatOpenAI

# from langchain.agents import initialize_agent, Tool, AgentType    # deprecated or about to be deprecated
from langchain_core.tools import Tool
# from langchain.agents import initialize_agent, AgentType    # deprecated or about to be deprecated
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    # before course upgradation:
    # agent = initialize_agent(
    #     tools=tools_for_agent,
    #     llm=llm,
    #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True,
    # )

    # after course upgradation:
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    # before course upgradation:
    # linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    # before course upgradation:
    # linked_profile_url = agent.invoke(
    #     input={
    #         "input":prompt_template.format_prompt(name_of_person=name)
    #         }
    #     )
    # return linked_profile_url

    # after course upgradation:
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url
