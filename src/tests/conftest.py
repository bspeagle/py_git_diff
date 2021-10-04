def pytest_addoption(parser):
    '''
    ???
    '''

    parser.addoption("--token", action="store", default="")


def pytest_generate_tests(metafunc):
    '''
    Define args available for cli
    '''

    option_value = metafunc.config.option.token
    if 'token' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("token", [option_value])
