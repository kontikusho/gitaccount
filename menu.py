#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Menu """
import inquirer
from config import Config


class Menu:
    """ Menu Class """

    _config = Config()

    def show(self):
        """ show list """
        choices = list(map(lambda x: x["account"], self._config.show()))
        choices.append(("Regist New Account", None))
        questions = [
            inquirer.List(
                "account",
                message="Select Your Git Account",
                choices=choices,
                carousel=True,
                default=choices[0],
            ),
        ]
        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return self._config.get(answers["account"])

    def add(self):
        """ add accouts """
        print("Regist New Account.")
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
        ]
        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return self._config.add(answers)

    def detail(self, account):
        """ show account detail """
        print("Detail Account.")
        print("Account name: " + account["account"])
        print("Author name: " + account["name"])
        print("Author email: " + account["email"])
        choices = [("Select"), "Edit", "Delete"]
        questions = [
            inquirer.List(
                "account",
                message="Select Your Git Account",
                choices=choices,
                carousel=True,
                default=choices[0],
            ),
        ]
        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        return answers


menu = Menu()
print(menu.detail({"account": "1", "name": "2", "email": "3"}))
