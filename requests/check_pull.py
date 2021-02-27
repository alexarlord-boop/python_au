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
        self.get_user_repos()
        self.curr_repo = None

    def get_user_repos(self):
        g = Github()
        user = g.get_user(self.name)

        self.repos = user.get_repos()

    def get_spec_repo(self, repo_name):
        for repo in self.repos:
            if repo.name == 'python_au':
                self.curr_repo = repo


if __name__ == '__main__':
    usernames = get_git_names()
    for name in usernames:
        validator = Validator(name)


        for rep in validator.repos:
            print(rep)
        print('--------------------')
