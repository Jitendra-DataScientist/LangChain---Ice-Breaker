# import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv


# dotenv_path = os.path.join(os.getcwd(), ".env")
# load_dotenv(dotenv_path)
# OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# print (OPENAI_API_KEY)

information="""Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. Musk is the founder,
 chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of
 Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and 
 OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of
  US$219 billion as of November 2023, according to the Bloomberg Billionaires Index, and $241 billion according to 
  Forbes, primarily from his ownership stakes in Tesla and SpaceX."""

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

    print(chain.run(information=information))
    
