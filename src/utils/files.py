#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by g7tianyi on 29/9/2018

import errno
import os
import shutil


class FileUtils:

    def __init__(self):
        raise Exception('Filer is a pure static class')

    @staticmethod
    def exists_directory(path):
        return os.path.isdir(path)

    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def copy_directory(src, dst):
        try:
            shutil.copytree(src, dst)
        except OSError as ex:  # python > 2.5
            if ex.errno == errno.ENOTDIR:
                shutil.copy(src, dst)
            else:
                raise

    @staticmethod
    def move_directory(src, dst):
        FileUtils.copy_directory(src, dst)
        FileUtils.remove_directory(src)

    @staticmethod
    def remove_directory(path):
        if FileUtils.exists_directory(path):
            shutil.rmtree(path)

    @staticmethod
    def exists_file(path):
        return os.path.isfile(path)

    @staticmethod
    def read_file(path):
        return open(path, 'r').read()

    @staticmethod
    def create_file(path, data):
        FileUtils.create_directory(os.path.dirname(path))
        with open(path, 'w') as f:
            f.write(data)

    @staticmethod
    def copy_file(src, dst):
        data = FileUtils.read_file(src)
        FileUtils.create_file(dst, data)

    @staticmethod
    def remove_file(path):
        os.remove(path)
