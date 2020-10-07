#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Config Loader/Saver """

import json
import os


class Config:
    """ Config class """

    path = os.environ["HOME"] + "/.gitaccount"
    config = []

    @classmethod
    def load(cls):
        """ Config loader """
        if not os.path.exists(cls.path):
            cls.save()
        with open(Config.path, "r") as _:
            cls.config = json.load(_)

    @classmethod
    def save(cls):
        """ Config Saver """
        with open(cls.path, "w") as _:
            json.dump(cls.config, _)
