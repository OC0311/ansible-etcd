#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by g7tianyi on 05/01/2018

from time import gmtime, strftime

NONE_COLOR = '\033[0m'
INFO_COLOR = '\033[1;36m'
WARN_COLOR = '\033[1;33m'
ERRO_COLOR = '\033[1;31m'


class Logger(object):

    def __init__(self):
        pass

    def debug(self, *args):
        print INFO_COLOR + '%s %s' % (self._meta('DEBU'), self._msg(*args)) + NONE_COLOR

    def info(self, *args):
        print '================================================================================'
        print '%s %s' % (self._meta('INFO'), self._msg(*args))
        print

    def warn(self, *args):
        print WARN_COLOR + '%s %s' % (self._meta('WARN'), self._msg(*args)) + NONE_COLOR

    def error(self, *args):
        print ERRO_COLOR + '%s %s' % (self._meta('ERRO'), self._msg(*args)) + NONE_COLOR

    def _meta(self, level):
        return '%s [%s] -' % (self.now(), level)

    @staticmethod
    def _msg(*args):
        return ' '.join([str(elem) for elem in list(args)])

    @staticmethod
    def now():
        return strftime('%Y-%m-%d %H:%M:%S%z', gmtime())


logger = Logger()
