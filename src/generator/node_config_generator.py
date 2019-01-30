#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by martin on 28/01/2019
import os
from src.utils import Jinja2

from src.logger import logger

NODECONFIGTEMPLATE = """name: {{ name }}
advertise-client-urls: http://{{ host }}:2379,http://127.0.0.1:2381
listen-client-urls: http://0.0.0.0:2379,http://127.0.0.1:2381
initial-advertise-peer-urls: http://{{ host }}:2380
listen-peer-urls: http://0.0.0.0:2380
initial-cluster-token: {{ token }}
initial-cluster: {{ cluster }}
initial-cluster-state: new
"""



class NodeConfigGenerator:

    def __init__(self, config):
        self.config = config

    def generate(self):
        # 循环生成文件
        configs = self.config.get_cluster_config()
        for config in configs:
            filename = config["name"]+"_config.yml"
            filename = os.path.join(self.config.config_dir, filename)
            logger.info('==>>【准备】1.1.0 生成节点配置文件 =>【%s】' % filename)
            Jinja2.flush(config, template=NODECONFIGTEMPLATE, filename=filename)
