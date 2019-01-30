#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by martin on 28/01/2019

import os
from src.utils import Jinja2

from src.logger import logger


HOSTSTEMPLATE = """[etcd]
{%- for node in nodes %}
{{ node.host }} node_name={{ node.name }}
{%- endfor %}
"""


class HostsConfigGenerator:

    def __init__(self, config):
        self.config = config

    def generate(self):
        filename = os.path.join(self.config.inventory_dir, 'hosts')
        logger.info('==>>【准备】1.1.0 生成主机清单文件 =>【%s】' % filename)
        Jinja2.flush(self.config.get_nodes(), template=HOSTSTEMPLATE, filename=filename)
