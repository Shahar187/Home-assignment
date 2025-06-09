import csv  # For writing data to CSV files
from datetime import datetime  # For generating timestamped filenames

import extract


#  Creates a dictionary from a single pull request object
def create_dictionary(pr):
    pr_number = pr['number']
    pr_title = pr['title']
    author = pr['user']['login']
    merge_date = pr['merged_at']
    cr_passed = extract.get_reviews_data(pr_number)
    checks_passed = extract.get_checks_passed(pr)

    pr_dic = {'PR number': pr_number,
              'PR title': pr_title,
              'Author': author,
              'Merge date': merge_date,
              'CR_Passed': cr_passed,
              'CHECKS_PASSED': checks_passed}

    return pr_dic


# Generates a CSV report containing data from all pull requests
def create_csv_report():
    pull_requests = extract.get_pr_data()  # Fetch all pull requests
    data = []

    for pr in pull_requests:
        pr_data = create_dictionary(pr)
        data.append(pr_data)

    # Define the CSV file name with a timestamp to make it unique
    with open(f'prDataReports/pr_data {date_time_str}.csv', 'w', newline='') as csv_file:
        field_names = ['PR number', 'PR title', 'Author', 'Merge date', 'CR_Passed', 'CHECKS_PASSED']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


# Get the current date and time to use in the report filename
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")

if __name__ == "__main__":
    create_csv_report()
