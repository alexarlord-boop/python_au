import requests
from github import Github


def get_git_names():
    names = list()
    with open('links.txt') as f:
        raw_links = f.readlines()
        for link in raw_links:
            names.append(link.split('/')[-1].strip('\n'))
    return names


class Validator:  # for one user
    def __init__(self, name):
        self.name = name
        self.repos = list()
        # self.get_user_repos()
        self.curr_repo = None
        self.TOKEN =

    # def get_user_repos(self):
    #     g = Github()
    #     user = g.get_user(self.name, )
    #     self.repos = user.get_repos()

    def get_spec_repo(self, repo_name):
        for repo in self.repos:
            if repo.name == repo_name:
                self.curr_repo = repo

    def prepare_headers(self):
        return {
            'Autorization': 'token {}'.format(self.TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
        }

    def get_pulls(self, repo_name):
        self.get_spec_repo(repo_name)
        url = f'https://api.github.com/repos/{self.name}/{repo_name}/pulls'
        r = requests.get(url, headers=self.prepare_headers())
        for pull in r.json():
            print(pull['title'])


if __name__ == '__main__':
    usernames = get_git_names()
    for name in usernames:
        validator = Validator(name)
        validator.get_pulls('python_au')
        print('--------------------')
