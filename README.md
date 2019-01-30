# ansible-etcd
利用ansible搭建etcd集群网络
# 准备工作

- 确保已经安装Docker环境
- 确保已经安装好Python开发环境
- 确保已经安装好Ansible环境

注：暂只支持CentOS一键部署

# 使用方法

1、编写集群部署配置文件（yml格式），放置在ansible-etcd 的cfg文件夹下

```

cluster: "etcd-clusterv"        # 集群名称
cluster_token: "token"          # 加入集群使用token
nodes:
  - host: 192.168.0.155         # 节点IP
    name: etcd-0                # 节点名称
  - host: 192.168.0.156
    name: etcd-1
  - host: 192.168.0.157
    name: etcd-2
```

2、进入到项目文件夹中执行

```
./start.sh -c config.yml

```

注：所有的操作都会在一个复制文件夹（workspace）下进行

