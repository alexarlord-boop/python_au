import requests
import json
from github import Github

CODE_WORDS = ['LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
ACTIONS = ['Added', 'Deleted', 'Fixed', 'Refactored', 'Moved']
GROUPS = ['1022', '1021']


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
        self.curr_rep = None
        self.TOKEN = 'e94a023059fec44f0283b00f2c9505ab8999ff4b'

    def prepare_headers(self):
        return {
            'Autorization': 'token {}'.format(self.TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
        }

    def prepare_body(self, pull, comment):
        return {
            'body': f"{comment}",
            'path': requests.get(pull['url'] + '/files', headers=self.prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pull['head']['sha']
        }

    def get_all_pulls(self):
        url = f'https://api.github.com/repos/{self.user}/python_au/pulls'
        pulls = requests.get(url, headers=self.prepare_headers()).json()
        return pulls

    def get_pull_commits(self, pull):
        url = pull['commits_url']
        raw_commits = requests.get(url, headers=self.prepare_headers()).json()
        return raw_commits

    def prepare_comment(self, message):
        res_comment = list()
        message_parts = message.split()
        code_word_g, action = message_parts[0], message_parts[1]
        code_word, group = code_word_g.split('-')

        if code_word not in CODE_WORDS:
            res_comment.append(f"! Message must start with code word in {CODE_WORDS}")

        if group not in GROUPS:
            res_comment.append(f"! Message must contain group number in {GROUPS}")

        if action not in ACTIONS:
            res_comment.append(f"! Message must start with {ACTIONS}")

    def post_pull_comment(self, pull, comment):
        url = f"https://api.github.com/repos/{self.user}/python_au/{pull['id']}/issue_comments"
        r = requests.post(pull['url'] + '/comments', headers=self.prepare_headers(),
                          data=json.dumps(self.prepare_body(pull, comment)).encode('utf8'))
        data = 'test comment'
        requests.post(url, data)

    def check_commit_message(self, pull):
        invalid_commits = list()
        for commit in self.get_pull_commits(pull):
            commit_message = commit['commit']['message']

            if not self.prepare_comment(commit_message):
                invalid_commits.append(commit_message)
        return invalid_commits

    def check_pulls(self):
        for pull in self.get_all_pulls():
            if len(self.check_commit_message(pull)) > 0:
                self.post_pull_comment(pull, comment)


if __name__ == '__main__':
    # usernames = get_git_usernames()
    usernames = ['alexarlord-boop', 'Vasis3038', 'l92169']

    validator = Validator(usernames[0])

# id 15
