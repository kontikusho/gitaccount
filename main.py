#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" test """
import subprocess
from account import Account
from config import Config
from prompt import Prompt


class Menu:
    """ Menu Class """

    transition = [
        {
            "trigger": "cancel",
            "source": "list",
            "dst": "end"
        },
        {
            "trigger": "select",
            "source": "list",
            "dst": "detail"
        },
        {
            "trigger": "add",
            "source": "list",
            "dst": "add"
        },
        {
            "trigger": "return",
            "source": "detail",
            "dst": "list"
        },
        {
            "trigger": "select",
            "source": "detail",
            "dst": "set"
        },
        {
            "trigger": "edit",
            "source": "detail",
            "dst": "edit"
        },
        {
            "trigger": "return",
            "source": "add",
            "dst": "list"
        },
        {
            "trigger": "return",
            "source": "edit",
            "dst": "list"
        },
        {
            "trigger": "end",
            "source": "set",
            "dst": "end"
        },
    ]

    def __init__(self):
        self.state_list = {
            "list": self.list,
            "detail": self.detail,
            "add": self.add,
            "edit": self.edit,
            "set": self.set,
            "end": None
        }
        self.config = Config()
        self.state = "list"
        self._args = None

    def run(self):
        """ run """
        if self.state == "end":
            return False
        ret = self.state_list[self.state](self._args)
        self.state = [
            x for x in self.transition
            if x['source'] == self.state and x['trigger'] == ret[0]
        ][0]['dst']
        self._args = ret[1]
        return True

    def list(self, _):
        """ a """
        config = self.config.show()
        account_list = list(map(lambda x: (x.account, x), config.values()))
        val = Prompt.list(account_list)
        if val is None:
            return ("add", None)
        if val is False:
            return ("cancel", None)
        return ("select", val)

    def detail(self, account: Account):
        """ test """
        val = Prompt.detail(account)
        if val == "edit":
            return ("edit", account)
        if val == "delete" and Prompt.remove():
            self.config.remove(account)
            self.config.save()
        if val == "select":
            return ("select", account)
        return ("return", None)

    def add(self, _):
        """ add """
        val = Prompt.add()
        if val['confirm']:
            self.config.add(Account.forge(val))
            self.config.save()
        return ("return", None)

    def edit(self, account: Account):
        """ edit """
        val = Prompt.edit(account)
        if val["confirm"]:
            self.config.edit(account.account, Account.forge(val))
        return ("return", None)

    def set(self, account: Account):
        """ set git config """
        val = Prompt.select()
        if val:
            subprocess.call(["git", "config", "user.name", account.name])
            subprocess.call(["git", "config", "user.email", account.email])
            return ("end", None)
        return ("return", None)


menu = Menu()

F = True
while F:
    F = menu.run()
