'''
Passing tests
'''

import os
from typing import Any
import pytest
from helpers.github import API

api = API()
pass_token = Any
pass_org = os.getenv('PASS_ORG')
pass_repo = os.getenv('PASS_REPO')


def test_pass_auth(token):
    '''
    Pass 'auth' to Github
    '''

    pass_token = token
    api.authenticate(pass_token)

    assert api._current_user is not None


def test_pass_org():
    '''
    Pass 'get organization'
    '''

    api.get_organization(pass_org)
    assert api._org.login == pass_org


def test_pass_repo():
    '''
    Pass 'get repo'
    '''

    api.get_organization(pass_org)
    api._repo.full_name == pass_repo
