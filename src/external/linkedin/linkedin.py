import json
import os
import re
from pathlib import Path

import requests

PROFILE_DIR = Path(__file__).parent / "profile_data"


def _extract_profile_name(linkedin_url: str) -> str | None:
    pattern = r"linkedin\.com/in/([^/]+)"
    match = re.search(pattern, linkedin_url)
    if match:
        return match.group(1)
    return None


def _get_from_local_storage(name: str) -> dict | None:
    file = PROFILE_DIR / f"{name}.json"
    profile = None
    if file.exists():
        with open(file) as source:
            profile = json.load(source)
    return profile


def _save_in_local_storage(name: str, profile: dict) -> bool:
    file = PROFILE_DIR / f"{name}.json"
    try:
        with open(file, mode="w") as sink:
            json.dump(profile, sink, indent=4)
            return True
    except Exception as e:
        print(e)
        return False


def fetch_linkedin_profile(linkedin_url):
    name = _extract_profile_name(linkedin_url)
    raw_profile = _get_from_local_storage(name)
    if raw_profile is not None:
        return raw_profile

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_key = os.environ["LINKEDIN_API_KEY"]
    header_dic = {"Authorization": "Bearer " + api_key}
    params = {"url": linkedin_url}
    response = requests.get(api_endpoint, params=params, headers=header_dic)

    raw_profile = json.loads(response.content)

    if response.status_code == 200:
        _save_in_local_storage(name, raw_profile)
    return raw_profile


def get_informative(raw_profile: dict) -> dict:
    profile = {}
    for k, v in raw_profile.items():
        if (v not in ([], "", None)) and (
            k not in ("certifications", "people_also_viewed")
        ):
            profile[k] = v

    groups: list[dict] = profile.get("groups")
    if groups:
        for g in groups:
            g.pop("profile_pic_url")

    return profile


def scrape_linkedin_profile(linkedin_url: str) -> dict:
    """scrape information from linkedin profile.
    it can manually read linkedin profile and get information"""

    raw_profile = fetch_linkedin_profile(linkedin_url)
    return get_informative(raw_profile)
