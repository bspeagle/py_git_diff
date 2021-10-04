'''
Failure tests
'''

import os
from typing import Any
import pytest
from helpers.github import API

api = API()
pass_token = Any
fail_token = os.getenv('FAIL_TOKEN')
fail_org = os.getenv('FAIL_ORG')
fail_repo = os.getenv('FAIL_REPO')


def test_fail_auth():
    '''
    Fail 'auth' to Github
    '''

    with pytest.raises(SystemExit):
        api.authenticate(fail_token)


def test_fail_org(token):
    '''
    Fail 'get organization'
    '''

    pass_token = token

    with pytest.raises(SystemExit):
        api.authenticate(pass_token)
        api.get_organization(fail_org)


def test_fail_repo():
    '''
    Fail 'get repo'
    '''

    with pytest.raises(SystemExit):
        api.get_repo("user", fail_repo)
