#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by martin on 28/01/2019
import yaml
import os


class Config:

    def __init__(self, filename):
        if not filename:
            raise Exception('请提供集群配置文件')

        with open(filename, 'r') as f:
            self.cluster = yaml.load(f)

        self.nodes = self.cluster["nodes"]
        self.cluster_name = self.cluster["cluster"]
        self.cluster_token = self.cluster["cluster_token"]
        # 路径配置
        self.project_dir = os.path.join(os.path.join(os.path.dirname(__file__), '../..'))
        self.workspace = os.path.join(os.path.join(os.path.dirname(__file__), '../..', 'workspace', 'etcd-cluster'))
        self.inventory_dir = os.path.join(self.workspace, 'inventories')
        self.config_dir = os.path.join(self.workspace, 'roles/upload/files')

    def get_config(self):

        return self

    def get_nodes(self):

        return {
            "nodes": self.nodes
        }

    def get_cluster_name(self):

        return {
            "cluster_name": self.cluster_name
        }

    def get_cluster_token(self):

        return {
            "cluster_token": self.cluster_token
        }

    # 获取集群
    def get_cluster_config(self):

        config_list = []

        nodes = self.get_nodes()["nodes"]
        token = self.get_cluster_token()["cluster_token"]

        # 生成集群列表
        cluster = ",".join([node["name"] + "=" + "http://"+node["host"] + ":2380" for node in nodes])
        for node in nodes:

            node_map = {
                "host": node["host"],
                "name": node["name"],
                "cluster": cluster,
                "token": token,
            }

            config_list.append(node_map)

        return config_list

