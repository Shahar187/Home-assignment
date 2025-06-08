import csv
from datetime import datetime

import extract


# This function create a pull request data dictionary
def create_dictionary(pr):
    pr_number = pr['number']
    pr_title = pr['title']
    author = pr['user']['login']
    merge_date = pr['merged_at']
    cr_passed = extract.get_reviews_data(pr_number)

    pr_dic = {'PR number': pr_number,
              'PR title': pr_title,
              'Author': author,
              'Merge date': merge_date,
              'CR_Passed': cr_passed}

    return pr_dic


now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")

# CREATE A FUNCTION- create_csv_report()
pull_requests = extract.get_pr_data()
data = []

for pr in pull_requests:
    pr_data = create_dictionary(pr)
    data.append(pr_data)

with open(f'repo_data {date_time_str}.csv', 'w', newline='') as csv_file:
    field_names = ['PR number', 'PR title', 'Author', 'Merge date', 'CR_Passed']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)
