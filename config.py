#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Config Loader/Saver """

import json
import os


class Config:
    """ Config class """

    _path = os.environ["HOME"] + "/.gitaccount"
    _config = []

    def __init__(self, path=None):
        """ init Method """
        self._path = path if path else self._path
        self.load()

    def load(self):
        """ Config load """
        if not os.path.exists(self._path):
            self.save()
        with open(self._path, "r") as _:
            self._config = json.load(_)

    def save(self):
        """ Config Save """
        with open(self._path, "w") as _:
            json.dump(self._config, _)

    def add(self, account, name, email):
        """ Add Account """
        if self.get(account):
            self.edit(account, name, email)
            return

        data = {"accountName": account, "name": name, "email": email}
        self._config.append(data)

    def edit(self, account, name, email):
        """ Edit Account """
        data = self.get(account)
        data["name"] = name
        data["email"] = email

    def get(self, account):
        """ Get Account """
        data = [x for x in self._config if x["accountName"] == account]
        return data[0] if data else None

    def remove(self, account):
        """ Remove Account """
        self._config = [x for x in self._config if x["accountName"] != account]

    def show(self):
        """ show List """
        return self._config


if __name__ == "__main__":
    pass
