#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Config Loader/Saver """

import json
import os


def format_data(account):
    """ Fromat Data """
    return {
        "account": account["account"],
        "name": account["name"],
        "email": account["email"],
    }


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

    def add(self, account):
        """ Add Account """
        if self.get(account["account"]):
            self.edit(account)
            return
        self._config.append(format_data(account))

    def edit(self, account):
        """ Edit Account """
        data = self.get(account["account"])
        data["name"] = account["name"]
        data["email"] = account["email"]

    def get(self, account):
        """ Get Account """
        data = [x for x in self._config if x["account"] == account]
        return data[0] if data else None

    def remove(self, account):
        """ Remove Account """
        self._config = [x for x in self._config if x["account"] != account]

    def show(self):
        """ show List """
        return self._config


if __name__ == "__main__":
    pass
