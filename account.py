#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Accout """
import json


class Account:
    """ struct account """
    def __init__(self, account_name, name, email):
        self.account = account_name
        self.name = name
        self.email = email

    @classmethod
    def forge(cls, account):
        """ static init """
        return cls(account['account'], account['name'], account['email'])

    def show(self):
        """ print account """
        print("Account Name: " + self.account)
        print("Author Name: " + self.name)
        print("Author Email: " + self.email)

    def to_json(self):
        """ ToJson """
        return {
            "account": self.account,
            "name": self.name,
            "email": self.email
        }


class AccountJSONEncoder(json.JSONEncoder):
    """ Account Json Encode """
    def default(self, o):
        """ encode """
        if isinstance(o, Account):
            return o.to_json()
        return super().default(o)
