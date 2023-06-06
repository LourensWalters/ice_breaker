from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv, find_dotenv

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if __name__ == "__main__":
    print("Hello LangChain")

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco Udemy")

    summary_template = """
        given the LinkedIn information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url)
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/harrison-chase-961287118/')

    print(chain.run(information=linkedin_data))

#%%
