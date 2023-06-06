import os
import requests
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)
PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile.
    """

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data