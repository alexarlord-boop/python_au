import requests
from github import Github

code_words = ['LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
actions = ['Added', 'Deleted', 'Fixed', 'Refactored', 'Moved']
groups = ['1022', '1021']


def get_git_usernames():
    names = list()
    with open('links.txt') as f:
        raw_links = f.readlines()
        for link in raw_links:
            names.append(link.split('/')[-1].strip('\n'))
    return names


class Validator:
    def __init__(self, user):
        self.user = user
        self.repos = list()
        # self.get_user_repos()
        self.curr_repo = None
        self.invalid_pulls = list()
        self.TOKEN = 'e94a023059fec44f0283b00f2c9505ab8999ff4b'

    def get_user_repos(self):
        g = Github()
        user = g.get_user(self.user)
        self.repos = user.get_repos()

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

    def get_all_pulls(self, repo_name):
        url = f'https://api.github.com/repos/{self.user}/{repo_name}/pulls'
        pulls = requests.get(url, headers=self.prepare_headers()).json()
        return pulls

    def get_invalid_pulls(self, repo_name):
        self.get_spec_repo(repo_name)
        invalid_pulls = list()
        # url = f'https://api.github.com/repos/{self.name}/{repo_name}/pulls'
        # r = requests.get(url, headers=self.prepare_headers())
        for pull in self.get_all_pulls(repo_name):
            if not self.is_valid_pull(pull['title']):
                invalid_pulls.append(pull)
        return invalid_pulls

    def is_valid_pull(self, pull):
        pull_parts = pull.split()
        code_word_g, action = pull_parts[0], pull_parts[1]
        code_word, group = code_word_g.split('-')
        return code_word in code_words and group in groups and action in actions


if __name__ == '__main__':
    usernames = get_git_usernames()
    for user in usernames:

        validator = Validator(user)
        invalid_pulls = validator.get_invalid_pulls('python_au')

        print(validator.user)
        for pull in invalid_pulls:
            print(pull['title'])
        print('-' * 20)
