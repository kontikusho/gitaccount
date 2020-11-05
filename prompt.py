#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Prompts """
import inquirer
from config import Account


class Prompt:
    """ Prompt Class """
    @classmethod
    def list(cls, accounts):
        """ list menu """
        print("---- Account List ----")
        accounts.append(("Regist New Account", None))
        accounts.append(("Cancel", False))
        questions = [
            inquirer.List(
                "account",
                message="Select Your Git Account",
                choices=accounts,
                carousel=True,
                default=accounts[0],
            )
        ]
        answer = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answer['account']

    @classmethod
    def detail(cls, account: Account):
        """ account detail """
        print("---- Detail Account ----")
        account.show()
        choices = [
            ("Set This Account", "select"),
            ("Edit This Account", "edit"),
            ("Delete This Account", "delete"),
            ("Cancel", "cancel"),
        ]
        questions = [
            inquirer.List(
                "choice",
                message="Choose Menu",
                choices=choices,
                carousel=True,
                default=choices[0],
            )
        ]
        answer = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answer['choice']

    @classmethod
    def add(cls):
        """ add accout """
        print("---- Regist New Account ----")
        questions = [
            inquirer.Text(
                "account",
                message="What's your Account name",
                validate=lambda _, x: x,
            ),
            inquirer.Text(
                "name",
                message="What's Author name",
                validate=lambda _, x: x,
            ),
            inquirer.Text(
                "email",
                message="What's Author Email address",
                validate=lambda _, x: x,
            ),
            inquirer.Confirm(
                "confirm",
                message="Add this account?",
                default=True,
            )
        ]
        answer = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answer

    @classmethod
    def edit(cls, account: Account):
        """ edit accout """
        print("---- Edit Account ----")
        questions = [
            inquirer.Text(
                "account",
                message="What's your Account name",
                default=account.account,
                validate=lambda _, x: x,
            ),
            inquirer.Text(
                "name",
                message="What's Author name",
                default=account.name,
                validate=lambda _, x: x,
            ),
            inquirer.Text(
                "email",
                message="What's Author Email address",
                default=account.email,
                validate=lambda _, x: x,
            ),
            inquirer.Confirm(
                "confirm",
                message="Save this account?",
                default=True,
            )
        ]
        answer = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answer

    @classmethod
    def remove(cls):
        """ remove account """
        questions = [
            inquirer.Confirm(
                "remove",
                message="Delete this account?",
                default=False,
            )
        ]
        answer = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answer

    @classmethod
    def select(cls):
        """ select account """
        questions = [
            inquirer.Confirm(
                "select",
                message="Set this account?",
                default=True,
            )
        ]
        answer = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answer
