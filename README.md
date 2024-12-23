# Github-integration-with-agent-

This repository contains two Python scripts designed to interact with the GitHub API. These scripts allow you to perform various tasks such as creating issues, assigning them, and listing repositories associated with an authenticated user.

Files Overview

1. integration.py

This script provides a set of functions to manage GitHub issues for a repository. It includes:

Authentication: Connects to the GitHub API using a personal access token.

Functions:

create_issue(repo_name, title, body): Creates a new issue in the specified repository.

assign_issue(repo_name, issue_number, assignees): Assigns an issue to specified GitHub users.

update_issue(repo_name, issue_number, new_title=None, new_body=None): Updates the title and/or body of an issue.

Logging: Records actions and errors to github_integration.log.

Example Usage:

repo_name = 'your_github_repo_name'  # Replace with your repository name
issue = create_issue(repo_name, 'New Project Task', 'Details about the new task.')
if issue:
    assign_issue(repo_name, issue.number, ['username'])  # Replace with GitHub username
    update_issue(repo_name, issue.number, new_title='Updated Project Task', new_body='Updated details.')

2. github import.py

This script demonstrates basic interaction with the GitHub API, focusing on authentication and repository listing:

Authentication: Uses a personal access token to log in to GitHub.

Repository Listing: Retrieves and prints a list of all repositories for the authenticated user.

Example Output:

Authenticated as: username
Repository: repo1
Repository: repo2
...

Prerequisites

Python 3.x installed on your system.

Install the PyGithub library:

pip install PyGithub

Generate a GitHub Personal Access Token and replace the placeholder in the scripts with your token.

Usage Instructions

Setup:

Replace the access_token placeholder in both scripts with your GitHub Personal Access Token.

For integration.py, update the repository name (repo_name) and GitHub username(s) as needed.

Run the scripts:

Execute integration.py to manage issues:

python integration.py

Execute github import.py to list repositories:

python github\ import.py

Notes

Ensure your personal access token has the necessary permissions (e.g., repo scope for private repositories).

Replace placeholder values (e.g., your_github_repo_name, username) with actual data.

Logging (integration.py)

Logs are saved in the github_integration.log file, containing information about successful operations and errors encountered during execution.

