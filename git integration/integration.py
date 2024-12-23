from github import Github
import logging

# Set up logging
logging.basicConfig(filename='github_integration.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Authentication
access_token = 'your_personal_access_token'  # Replace with your token
g = Github(access_token)

# Function to create a GitHub issue
def create_issue(repo_name, title, body):
    try:
        repo = g.get_repo(repo_name)
        issue = repo.create_issue(title=title, body=body)
        logging.info(f"Issue created: {issue.title}")
        return issue
    except Exception as e:
        logging.error(f"Error creating issue: {e}")
        return None

# Function to assign issue to a user
def assign_issue(repo_name, issue_number, assignees):
    try:
        repo = g.get_repo(repo_name)
        issue = repo.get_issue(number=issue_number)
        issue.edit(assignees=assignees)
        logging.info(f"Issue {issue_number} assigned to: {assignees}")
        return issue
    except Exception as e:
        logging.error(f"Error assigning issue {issue_number}: {e}")
        return None

# Function to update an issue's title or body
def update_issue(repo_name, issue_number, new_title=None, new_body=None):
    try:
        repo = g.get_repo(repo_name)
        issue = repo.get_issue(number=issue_number)
        issue.edit(title=new_title, body=new_body)
        logging.info(f"Issue {issue_number} updated: Title - {new_title}, Body - {new_body}")
        return issue
    except Exception as e:
        logging.error(f"Error updating issue {issue_number}: {e}")
        return None

# Test the functions
if _name_ == '_main_':
    repo_name = 'your_github_repo_name'  # Replace with your repository name
    issue = create_issue(repo_name, 'New Project Task', 'Details about the new task.')
    if issue:
        assign_issue(repo_name, issue.number, ['username'])  # Replace with GitHub username
        update_issue(repo_name, issue.number, new_title='Updated Project Task', new_body='Updated details.')