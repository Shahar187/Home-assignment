# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()
import requests


#functions
def api_connect(url, headers):
    response = requests.get(url, headers=headers)
    return response


def get_pr_data(request):
    # If status_code is 200 we made a successful request!
    if request.status_code == 200:
        pull_requests = pull_requests_response.json()
        print(f"Retrieved {len(pull_requests)} pull requests for organization '{org_name}'.")
        for pr in pull_requests[:5]:  # Show first 5 repos for brevity
            print(pr['title'])

    # If status_code is not 200, something is wrong with our request
    else:
        print(f"Failed to retrieve pull request. Status code: {pull_requests_response.status_code}")
    return pull_requests


def get_reviews_data(pr_number):
    reviews_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"
    reviews_response = api_connect(reviews_url, headers=headers)

    if reviews_response.status_code == 200:
        reviews = reviews_response.json()
        approved = any(r['state'] == 'APPROVED' for r in reviews)

        if approved:
            return 'Approved'
        else:
            return "not approved"
    else:
        return "Can not fetch reviews"


#repository and pull request data
owner = "Scytale-exercise"
repo = "scytale-repo3"
org_name = "Scytle"

#API URL for the get request function
pull_request_data_url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all"

#Authentication
headers = {
    "Authorization": os.getenv("ACCESS_TOKEN"),
    "Accept": "application/vnd.github.v3+json"
}

# Make the API request. Note the .get() function, which corresponds to the HTTP method of our request
pull_requests_response = api_connect(pull_request_data_url, headers=headers)

#Get the pull request data
pull_requests = get_pr_data(pull_requests_response)

