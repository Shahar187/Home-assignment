import os  # For accessing environment variables

import requests  # For sending HTTP requests to the GitHub API
from dotenv import load_dotenv  # To load variables from a .env file

# Load environment variables from .env file
load_dotenv()


# Functions

# Send a GET request to the given URL
def fetch_information(url, headers):
    response = requests.get(url, headers=headers)
    return response


# Retrieves all pull requests from the repository
def get_pr_data():
    url = f"{base_url}?state=all"
    response = fetch_information(url, headers=headers)

    # If status_code is 200 we made a successful request!
    if response.status_code == 200:
        pull_requests = response.json()

    # If status_code is not 200, something is wrong with the request
    else:
        print(f"Failed to retrieve pull request. Status code: {response.status_code}")
        return []
    return pull_requests


# Retrieves review status for a specific pull request by PR number
def get_reviews_data(pr_number):
    url = f"{base_url}/{pr_number}/reviews"
    response = fetch_information(url, headers=headers)

    # If status_code is 200 we made a successful request!
    if response.status_code == 200:
        reviews = response.json()
        # Check if any review has the state 'APPROVED'
        approved = any(r['state'] == 'APPROVED' for r in reviews)

        if approved:
            return 'Approved'
        else:
            return "not approved"
    else:
        return "Can not fetch reviews"


# Define the owner and repo name to be used in the GitHub API URL
owner = "Scytale-exercise"
repo = "scytale-repo3"

# Base URL for accessing pull requests
base_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

# Authentication information
headers = {
    "Authorization": os.getenv("ACCESS_TOKEN"),
    "Accept": "application/vnd.github.v3+json"
}
