"""
Start up tasks
"""

import os
from dotenv import load_dotenv
from helpers.logger import LOGGER


def load_env_vars():
    """
    Load system and .env vars
    """

    try:
        if not bool(os.getenv('DOTENV_LOADED')):
            load_dotenv()
            LOGGER.debug('Module dotenv Loaded!')
            os.environ['DOTENV_LOADED'] = str(True)
        else:
            LOGGER.debug('Module dotenv already loaded.')
    except Exception as ex:
        raise ex
