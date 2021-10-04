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

    def load_organization(self, org):
        '''
        Get the org. Now. Do it.
        '''

        try:
            self.__org = self.__github.get_organization(self, org)
        except Exception as ex:
            LOGGER.error(f'{ex.args[1]["message"]} - Org: {org}')
            sys.exit("Fail. Try Again.")

    def test(self, args):
        '''
        Testes... Testes... 1, 2, 3...
        '''

        self.authenticate(args.t)

        if args.o:
            self.load_organization(args.o)
            LOGGER.info(self.__org.get_repo(args.r).description)
        else:
            LOGGER.info(self.__github.get_user(self).login)
            LOGGER.info(self.__github.get_repo(
                self, f'{self.__current_user}/{args.r}').description)
