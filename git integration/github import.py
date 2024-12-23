from github import Github

# Authenticate with your Personal Access Token
access_token = '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'  # Replace with your token
g = Github(access_token)

# Test authentication by fetching the authenticated user's information
user = g.get_user()
print(f'Authenticated as: {user.login}')

# List repositories of the authenticated user
for repo in user.get_repos():
    print(f'Repository: {repo.name}')