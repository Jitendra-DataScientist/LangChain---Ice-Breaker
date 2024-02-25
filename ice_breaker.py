import os
# from langchain import PromptTemplate    # deprecated or about to be deprecated
from langchain.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI    # deprecated or about to be deprecated
# from langchain_community.chat_models import ChatOpenAI    # deprecated or about to be deprecated
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from third_parties.linkedin_bypass import scrape_linkedin_profile


dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
print (OPENAI_API_KEY)


if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """
            given the {information} about a person from I want you to create:
            1. a short summary
            2. 2 interesting facts about them
        """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile()

    # before course upgradation:
    # print(chain.run(information=linkedin_data))
    
    # after course upgradation:
    res = chain.invoke(input={"information": linkedin_data})
    print(res["text"])
