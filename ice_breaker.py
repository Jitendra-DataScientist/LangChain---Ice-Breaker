import os
# from langchain import PromptTemplate    # deprecated or about to be deprecated
from langchain.prompts import PromptTemplate    # deprecated or about to be deprecated
from langchain_core.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI    # deprecated or about to be deprecated
# from langchain_community.chat_models import ChatOpenAI    # deprecated or about to be deprecated
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets


dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# print (OPENAI_API_KEY)


name = "Harrison Chase"
if __name__ == "__main__":
    print("Hello LangChain!")

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)

    summary_template = """
         given the Linkedin information {linkedin_information} and twitter {twitter_information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them 
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
    )

    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # before course upgradation:
    # print(chain.run(information=linkedin_data))

    # after course upgradation:
    res = chain.invoke(input={"information": linkedin_data})
    print(res["text"])
