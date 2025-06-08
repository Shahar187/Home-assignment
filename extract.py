# importing os module for environment variables
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()
import requests


# functions
def fetch_information(url, headers):
    response = requests.get(url, headers=headers)
    return response


def get_pr_data():
    url = f"{base_url}?state=all"
    response = fetch_information(url, headers=headers)

    # If status_code is 200 we made a successful request!
    if response.status_code == 200:
        pull_requests = response.json()

    # If status_code is not 200, something is wrong with our request
    else:
        print(f"Failed to retrieve pull request. Status code: {response.status_code}")
    return pull_requests


def get_reviews_data(pr_number):
    url = f"{base_url}/{pr_number}/reviews"
    response = fetch_information(url, headers=headers)

    if response.status_code == 200:
        reviews = response.json()
        approved = any(r['state'] == 'APPROVED' for r in reviews)

        if approved:
            return 'Approved'
        else:
            return "not approved"
    else:
        return "Can not fetch reviews"


# repository and pull request data
owner = "Scytale-exercise"
repo = "scytale-repo3"

# API URL for the get request function
base_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

# Authentication
headers = {
    "Authorization": os.getenv("ACCESS_TOKEN"),
    "Accept": "application/vnd.github.v3+json"
}
