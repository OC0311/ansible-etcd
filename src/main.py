#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by martin on 28/01/2019

import argparse
from src.generator import Config
from src.generator import HostsConfigGenerator
from src.generator import NodeConfigGenerator

if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, help='配置文件，请使用绝对路径')

    args = parser.parse_args()

    config = Config(filename=args.config).get_config()
    HostsConfigGenerator(config=config).generate()
    NodeConfigGenerator(config=config).generate()

