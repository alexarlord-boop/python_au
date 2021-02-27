import requests
from github import Github


class Validator():
    def __init__(self):
        self.names = list()
        self.current_repo = list()
        self.get_git_names()

    # Github usernames
    def get_git_names(self):
        with open('links.txt') as f:
            raw_links = f.readlines()
            for link in raw_links:
                self.names.append(link.split('/')[-1].strip('\n'))

    def get_user_repos(self, name):
        g = Github()
        user = g.get_user(name)
        for repo in user.get_repos():
            self.current_repo.append(repo)
