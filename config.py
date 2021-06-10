# config.py
# pylint: disable=missing-docstring

import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # The replace() call is to ensure that the URI starts with 'postgresql://' and not just 'postgres://' as it used to be (this is a back-compability hack)
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://", 1)
