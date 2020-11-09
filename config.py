#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Config Loader/Saver """

import json
import os
from account import Account, AccountJSONEncoder


class Config:
    """ Config class """

    _path = os.environ["HOME"] + "/.gitaccount"
    _config = {}

    def __init__(self, path=None):
        """ init Method """
        self._path = path if path else self._path
        self.load()

    def load(self):
        """ Config load """
        if not os.path.exists(self._path):
            self.save()
        with open(self._path, "r") as _:
            self._config = {
                k: Account.forge(v)
                for k, v in json.load(_).items()
            }

    def save(self):
        """ Config Save """
        with open(self._path, "w") as _:
            json.dump(self._config, _, cls=AccountJSONEncoder)

    def add(self, account: Account):
        """ Add Account """
        self._config[account.account] = account

    def edit(self, account_name, account: Account):
        """ Edit Account """
        del self._config[account_name]
        self._config[account.account] = account

    def get(self, account: Account):
        """ Get Account """
        return self._config[
            account.account] if account.account in self._config else False

    def remove(self, account: Account):
        """ Remove Account """
        self._config = [x for x in self._config if x != account]

    def show(self):
        """ show List """
        return self._config


if __name__ == "__main__":
    pass
