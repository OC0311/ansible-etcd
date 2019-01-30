#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by g7tianyi on 29/9/2018

import os

from jinja2 import Template
from files import FileUtils


class Jinja2:

    def __init__(self):
        pass

    @staticmethod
    def flush(args, template, filename=None, **other):
        content = Template(template).render(args, **other)
        if filename is not None:
            FileUtils.create_directory(os.path.dirname(filename))
            with open(filename, 'w') as f:
                f.write(content)
        return content

    @staticmethod
    def render(args, template):
        return Template(template).render(args)
