#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by g7tianyi on 26/01/2018

import random
import string
import time

from time import gmtime, strftime


def chars(choices, size):
    return ''.join([random.choice(choices) for _ in range(size)])


class RandUtils:

    def __init__(self):
        pass

    @staticmethod
    def string(size=8):
        return ''.join([random.choice('0123456789abcdef') for _ in range(size)])

    @staticmethod
    def int(mini=0, maxi=100):
        return random.randint(mini, maxi)

    @staticmethod
    def long(minl=0, maxl=10000):
        return random.randint(minl, maxl)

    @staticmethod
    def float(minf=0, maxf=10000):
        return round(random.uniform(minf, maxf), 2)

    @staticmethod
    def boolean():
        return RandUtils.int() > 50

    @staticmethod
    def timestamp():
        return (int(time.time()) - random.randint(60 * 60 * 24, 60 * 60 * 24 * 7)) * 1000
