# from langchain.serpapi import SerpAPIWrapper    # deprecated or about to be deprecated
from langchain_community.utilities.serpapi import SerpAPIWrapper


def get_profile_url(name: str) -> str:
    """Searches for Linkedin Profile Page."""
    search = SerpAPIWrapper()
    res = search.run(f"{name}")
    return res
