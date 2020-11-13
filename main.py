import os
import logging

logger = logging.getLogger(__name__)

a_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'

try:
    1 / 0
except:
    pass


def print_env():
    for i in os.environ:
        logger.exception(f'k={i}, v={os.environ[i]}')


def print_vars():
    logger.exception(f'locals={locals()}, globals={globals()}')


def print_data():
    print_env()
    print_vars()


print_data()
