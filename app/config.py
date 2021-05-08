"""Application configurations."""

import os
from secrets import token_hex

class Config():
    def __init__(self):
        self._login_secret = token_hex(32)
        self._mongodb_host = "localhost"
        self._mongodb_port = 27017
        self._base_dir = os.path.abspath(os.path.dirname(__file__))

    @property
    def mongo_uri(self):
        return f"mongodb://{self._mongodb_host}:{self._mongodb_port}/"
    
    @property
    def login_secret(self):
        return self._login_secret
    
    @property
    def base_dir(self):
        return self._base_dir