import requests
import json

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
    def __init__(self, user, repo_name, state):
        self.user = user
        self.repo_name = repo_name
        self.state = state
        self.repos = list()
        self.curr_pull_commits = list()
        self.TOKEN = 'bd6a331779d1f805f30d1db7eb50bbe131d3a501'

        self.pulls = self.get_all_pulls()

    def prepare_headers(self):
        return {
            'Autorization': 'token {}'.format(self.TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
        }

    def prepare_body(self, pull, comment):
        # print(pull['head'])
        return {
            'body': f"{comment}",
            'path': requests.get(pull['url'] + '/files', headers=self.prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pull['head']['sha']
        }

    def get_all_pulls(self):
        url = f'https://api.github.com/repos/{self.user}/{self.repo_name}/pulls'
        pulls = requests.get(url, headers=self.prepare_headers()).json()
        return pulls

    def get_pull_commits(self, pull):
        url = pull['commits_url']
        raw_commits = requests.get(url, headers=self.prepare_headers()).json()
        return raw_commits

    def check_prefixes(self, message):
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

        if len(res_comment) != 0:
            res_comment.insert(0, f"** Invalid Commit Message: {message} **")
            return '\n'.join(res_comment)
        else:
            return None

    def check_pull_commits(self, pull):
        comments = list()
        self.curr_pull_commits = self.get_pull_commits(pull)
        for commit in self.curr_pull_commits:
            comment = self.check_prefixes(commit['commit']['message'])
            if comment is not None:
                comments.append(comment)
        if len(comments) != 0:
            comments.insert(0, f"* Invalid PULL Commits: *")
            # print('\n\n'.join(comments))
            return '\n\n'.join(comments)
        return ''

    def send_pr_comment(self, pull, comment):
        if len(comment) != 0:
            url = pull['url'] + '/comments'

            r = requests.post(url, headers=self.prepare_headers(),
                              data=json.dumps(self.prepare_body(pull, comment)).encode('utf8'))
            print(r.json())
            print(url)


if __name__ == '__main__':
    # usernames = get_git_usernames()
    usernames = ['alexarlord-boop', 'Vasis3038', 'l92169']

    validator = Validator(usernames[0], 'python_au', 'all')
    validator.get_all_pulls()
    for pull in validator.pulls:
        validator.send_pr_comment(pull, validator.check_pull_commits(pull))
