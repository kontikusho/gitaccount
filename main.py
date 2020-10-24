#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Select Account UI """
import subprocess
import inquirer
from config import Config

config = Config()


def require(_, current):
    """ require Answer """
    return current


def main():
    """ main Program """
    # Select Account
    choices = list(map(lambda x: x["account"], config.show()))
    choices.append(("Regist New Account", None))
    answers = inquirer.prompt(
        [
            inquirer.List(
                "account",
                message="Select Your Git Account",
                choices=choices,
                carousel=True,
                default=choices[0],
            )
        ]
    )

    if not answers:
        return None

    # Regitst Account
    if not answers["account"]:
        questions = [
            inquirer.Text(
                "account",
                message="What's your Account name",
                validate=lambda _, x: x,
            ),
            inquirer.Text(
                "name",
                message="What's your name",
                validate=lambda _, x: x,
            ),
            inquirer.Text(
                "email",
                message="What's your Email address",
                validate=lambda _, x: x,
            ),
        ]
        answers = inquirer.prompt(questions)
        config.add(answers)
        config.save()

    account = config.get(answers["account"])
    subprocess.call(["git", "config", "user.name", account["name"]])
    subprocess.call(["git", "config", "user.email", account["email"]])
    return None


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
