'''
Utility to get git-diff between 2 commits
'''

from helpers.arparse import args
from helpers.github import API

api = API()

api.test(args)
