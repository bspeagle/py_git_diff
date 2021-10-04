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
        self.__org = github.Organization.Organization
        self.__repo = github.Repository.Repository
        self.__current_user = ""

    def authenticate(self, token):
        '''
        Authenticate to Github with access token
        '''

        LOGGER.debug(f'Token: {token}')

        self.__access_token = token

        try:
            self.__github.__init__(self, self.__access_token)
            self.__current_user = self.__github.get_user(self).login
            LOGGER.debug(
                f'Login Successful! Current User: {self.__current_user}')
        except Exception as ex:
            LOGGER.error(
                f'{ex.args[1]["message"]} - Token: {self.__access_token}')
            sys.exit("Fail. Try Again.")

    def get_organization(self, org):
        '''
        Get the org. Now. Do it.
        '''

        try:
            self.__org = self.__github.get_organization(self, org)
        except Exception as ex:
            LOGGER.error(f'{ex.args[1]["message"]} - Org: {org}')
            sys.exit("Fail. Try Again.")

    def get_repo(self, repo_type, repo_arg):
        '''
        Retrieve the repo. Or die trying.
        '''

        try:
            if repo_type == "org":
                self.__repo = self.__org.get_repo(repo_arg)
            elif repo_type == "user":
                self.__repo = self.__github.get_repo(self, repo_arg)
        except Exception as ex:
            LOGGER.error(f'{ex.args[1]["message"]} - Repo: {repo_arg}')
            sys.exit("Fail. Try Again.")

    def compare_commits(self, base_commit, head_commit):
        '''
        Compare commits and return commit messages
        '''

        try:
            self.__repo.get_commit(base_commit)
            self.__repo.get_commit(head_commit)
        except Exception as ex:
            LOGGER.error(ex.args[1]["message"])

        this_array = []

        compare_commits = self.__repo.compare(base_commit, head_commit).commits
        for commit in compare_commits:
            summary_commit = self.__repo.get_commit(commit.sha)

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
            self.get_repo("user", f'{self.__current_user}/{args.r}')

        return self.compare_commits(args.bc, args.hc)
