'''
Utility to get git-diff between 2 commits
'''

from helpers.arparse import args
from helpers.github import API
from helpers.logger import LOGGER

api = API()

diffs = api.git_diff(args)
LOGGER.info('--COMMITS--')
for diff in diffs:
    LOGGER.info(f'{diff["last_modified"]} - {diff["sha"]} - {diff["message"]}')
