"""
 GitHub PR Analyzer - Maintainer Notes
----------------------------------------
This script fetches and processes GitHub Pull Request data for a given repository.
It outputs a CSV report including PR number, title, author, merge date, code review status, and check status.

Maintainer Tips:
- If the GitHub API rate limits you, check if your ACCESS_TOKEN is still valid.
- Make sure the repository has enabled required checks (CI, linting) so that check-run data is meaningful.
- If you add more fields, remember to update both create_dictionary() and the CSV fieldnames.

Dependencies:
- requests
- python-dotenv
- csv, datetime
- A .env file with ACCESS_TOKEN

Author: Shahar Shitrit
Last updated: 2025-06-09
"""
