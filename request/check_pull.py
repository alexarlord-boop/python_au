import requests
import json
from datetime import datetime

CODE_WORDS = ['LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
ACTIONS = ['Added', 'Deleted', 'Fixed', 'Refactored', 'Moved']
GROUPS = ['1021', '1022']
TOKEN = '429088fa5f1fcbb5dbfc41d8e9746c4263b271f0'


def get_git_usernames():
    names = list()
    with open('links.txt') as f:
        raw_links = f.readlines()
        for link in raw_links:
            names.append(link.split('/')[-1].strip('\n'))
    return names


def prepare_headers():
    return {
        "Authorization": 'token {}'.format(TOKEN),
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    }


def prepare_body(pull, comment):
    return {
        'body': f"{comment}",
        'path': requests.get(pull['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
        'position': 1,
        'commit_id': pull['head']['sha']
    }


def get_all_user_prs(user_login, repo_name, pr_state):
    url = f'https://api.github.com/repos/{user_login}/{repo_name}/pulls?state={pr_state}'
    prs = requests.get(url, headers=prepare_headers())
    return prs.json()


def get_all_pr_commits(pr):
    return requests.get(pr['commits_url'], headers=prepare_headers()).json()


def check_prefixes(message):
    res_comment = list()
    message_parts = message.split()
    prefix_parts = message_parts[0].split('-')
    if len(prefix_parts) == 1:
        prefix_parts.append('')
    elif len(prefix_parts) != 2:
        prefix_parts = ['', '']
    task, group = prefix_parts

    if task not in CODE_WORDS:
        res_comment.append(f"! Message must start with code word in {CODE_WORDS}")

    if group not in GROUPS:
        res_comment.append(f"! Message must contain group number in {GROUPS}")

    if len(message_parts) == 1 or message_parts[1] not in ACTIONS:
        res_comment.append(f"! Message must start with {ACTIONS}")

    if len(res_comment) != 0:
        res_comment.insert(0, f"** Invalid Commit Message: {message} **")
        return '\n'.join(res_comment)
    return ''


def verify_pr(pr):
    comments = list()
    all_commits = get_all_pr_commits(pr)
    for commit in all_commits:
        comment = check_prefixes(commit['commit']['message'])
        if len(comment) > 0:
            comments.append(comment)
    if len(comments) != 0:
        comments.insert(0, f"# Invalid PULL Commits")
        send_pr_comment(pr, '\n\n'.join(comments))


def send_pr_comment(pull, comment):
    url = pull['url'] + '/comments'
    r = requests.post(url, headers=prepare_headers(),
                      data=json.dumps(prepare_body(pull, comment)))
    return pull['html_url']


def str_to_date(date):
    frmt = "%Y-%m-%dT%H:%M:%SZ"
    return datetime.strptime(date, frmt)


def get_comment_date_by(pr, author):
    r = requests.get(pr['review_comments_url']).json()

    if len(r) > 0:
        if r[-1]['user']['login'] == author:
            return str_to_date(r[-1]['created_at'])
    return None


def get_commit_date(commit):
    return str_to_date(commit['commit']['author']['date'])


def check_new_commits(pr, date):
    comments = list()
    all_commits = get_all_pr_commits(pr)
    for commit in all_commits:
        if get_commit_date(commit) > date:
            comment = check_prefixes(commit['commit']['message'])
            if len(comment) > 0:
                comments.append(comment)

    if len(comments) != 0:
        comments.insert(0, f"# VERIFICATION RESULT: ")
        send_pr_comment(pr, '\n\n'.join(comments))


if __name__ == '__main__':
    repo_name = 'python_au'
    usernames = ['alexarlord-boop', 'Vasis3038', 'l92169']
    state = 'open'
    reviewer = 'alexarlord-boop'

    # for user in usernames:
    #     pulls = get_all_user_prs(user, repo_name, state)
    #     for pr in pulls:
    #         # проверка на наличие комментариев
    #         verify_pr(pr)

    pulls = get_all_user_prs(usernames[0], repo_name, state)
    for pr in pulls:
        comment_date = get_comment_date_by(pr, reviewer)
        if comment_date is not None:
            check_new_commits(pr, comment_date)
        else:
            verify_pr(pr)