'''
Github API Module
'''

import sys
import github
from helpers.logger import LOGGER


class API:
    '''
    Github API actions
    '''

    def __init__(self):
        self.__access_token = str
        self.__github = github.Github
        self._org = github.Organization.Organization
        self._repo = github.Repository.Repository
        self._current_user = ""

    def authenticate(self, token):
        '''
        Authenticate to Github with access token
        '''

        LOGGER.debug(f'Token: {token}')

        self.__access_token = token

        try:
            self.__github.__init__(self, self.__access_token)
            self._current_user = self.__github.get_user(self).login
            LOGGER.debug(
                f'Login Successful! Current User: {self._current_user}')
        except Exception as ex:
            LOGGER.error(
                f'{ex.args[1]["message"]} - Token: {self.__access_token}')
            sys.exit("Fail. Try Again.")

    def get_organization(self, org):
        '''
        Get the org. Now. Do it.
        '''

        try:
            self._org = self.__github.get_organization(self, org)
        except Exception as ex:
            LOGGER.error(f'{ex.args[1]["message"]} - Org: {org}')
            sys.exit("Fail. Try Again.")

    def get_repo(self, repo_type, repo_arg):
        '''
        Retrieve the repo. Or die trying.
        '''

        try:
            if repo_type == "org":
                self._repo = self._org.get_repo(repo_arg)
            elif repo_type == "user":
                self._repo = self.__github.get_repo(self, repo_arg)
        except Exception as ex:
            LOGGER.error(f'{ex.args[1]["message"]} - Repo: {repo_arg}')
            sys.exit("Fail. Try Again.")

        LOGGER.info(self._repo)

    def compare_commits(self, base_commit, head_commit):
        '''
        Compare commits and return commit messages
        '''

        try:
            self._repo.get_commit(base_commit)
        except Exception as ex:
            LOGGER.error(f'Base Commit - {ex.args[1]["message"]}')
            sys.exit("Fail. Try Again.")
        try:
            self._repo.get_commit(head_commit)
        except Exception as ex:
            LOGGER.error(f'Head Commit - {ex.args[1]["message"]}')
            sys.exit("Fail. Try Again.")

        this_array = []

        compare_commits = self._repo.compare(base_commit, head_commit).commits
        for commit in compare_commits:
            summary_commit = self._repo.get_commit(commit.sha)

            this_array.append({
                "sha": summary_commit.sha,
                "message": summary_commit.commit.message,
                "last_modified": summary_commit.last_modified
            })

        return this_array

    def git_diff(self, args):
        '''
        Get diffs: sha, message, last modified date
        '''

        self.authenticate(args.t)

        if args.o:
            self.get_organization(args.o)
            self.get_repo("org", args.r)
        else:
            self.get_repo("user", f'{self._current_user}/{args.r}')

        return self.compare_commits(args.bc, args.hc)
