import requests
from github import Github


# Github usernames
def get_git_names():
    names = list()
    with open('links.txt') as f:
        raw_links = f.readlines()
        for link in raw_links:
            names.append(link.split('/')[-1].strip('\n'))
    return names


usernames = get_git_names()
for username in usernames:

    g = Github()
    user = g.get_user(username)
    for repo in user.get_repos():
        print(repo)
