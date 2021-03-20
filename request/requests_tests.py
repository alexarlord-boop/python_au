import unittest
import json
from request.check_pull import CODE_WORDS, ACTIONS, GROUPS
from request.check_pull import get_comment_date, get_all_pr_commits, get_all_user_prs, check_prefixes


class TestCheckPrefixes(unittest.TestCase):
    def test_check(self):
        message1 = 'LEETCODE-1022 Added smth'
        self.assertEqual(check_prefixes(message1), '')

        message2 = 'LEETCODE-1022 Addedwef '
        self.assertEqual(check_prefixes(message2),
                         f"** Invalid Commit Message: {message2} **\n" + f"! Message must start with {ACTIONS}")

        message3 = 'LEETCODE-102 Added smth'
        self.assertEqual(check_prefixes(message3),
                         f"** Invalid Commit Message: {message3} **\n" + f"! Message must contain group number in {GROUPS}")

        message4 = 'LEET-1022 Added smth'
        self.assertEqual(check_prefixes(message4),
                         f"** Invalid Commit Message: {message4} **\n" + f"! Message must start with code word in {CODE_WORDS}")


class TestGetUserPrs(unittest.TestCase):

    def test_get_prs(self):
        prs = get_all_user_prs('alexarlord-boop', 'python_au', 'open')  # json
        with open('test_data.txt') as f:
            test_prs = json.loads(f.read())
        self.assertEqual(prs, test_prs)


