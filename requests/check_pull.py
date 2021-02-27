import requests
from github import Github


def get_git_names():
    names = list()
    with open('links.txt') as f:
        raw_links = f.readlines()
        for link in raw_links:
            names.append(link.split('/')[-1].strip('\n'))
    return names


class Validator():  # for one user
    def __init__(self, name):
        self.name = name
        self.repos = list()

    # Github usernames

    def get_user_repos(self):
        g = Github()
        user = g.get_user(self.name)

        for repo in user.get_repos():
            self.repos.append(repo)


if __name__ == '__main__':
    usernames = get_git_names()
    for name in usernames:
        validator = Validator(name)
        validator.get_user_repos()
        print(validator.repos)
        print('--------------------')
