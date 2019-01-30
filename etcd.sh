#!/bin/bash
# Created by martin on 24/01/2019

set -e

pushd $(dirname $0) > /dev/null
SCRIPTPATH=$(pwd -P)
popd > /dev/null
SCRIPTFILE=$(basename $0)

function log() {
    echo "================================================================================"
    echo "$(date +'%Y-%m-%d %H:%M:%S%z') [INFO] - $@"
    echo ""
}

function err() {
    echo "================================================================================"
    echo "$(date +'%Y-%m-%d %H:%M:%S%z') [ERRO] - $@" >&2
}


# initial-advertise-peer-urls 对等节点接受消息的url 发送
# listen-peer-urls 接受对等节点的消息的url 接受

function run() {

    docker run  -d  -p 4001:4001 -p 2380:2380 -p 2379:2379 --name etcd quay.io/coreos/etcd:v3.3.10 etcd -name etcd0 \

    -initial-advertise-peer-urls http://0.0.0.0:2380 \
    -listen-peer-urls http://0.0.0.0:2380 \
    -listen-client-urls http://0.0.0.0:2379,http://127.0.0.1:2379 \
    -advertise-client-urls http://0.0.0.0:2379 \
    -initial-cluster-token etcd-cluster-1 \
    -initial-cluster etcd0=http://0.0.0.0:2380,etcd0=http://0.0.0.0:2381,etcd0=http://0.0.0.0:2382 \
    -initial-cluster-state new

}


function run2(){

    docker run  -d  -p 4001:4001 -p 2380:2380 -p 2379:2379 --name etcd quay.io/coreos/etcd:v3.3.10 etcd -name etcd0 \
    -advertise-client-urls http://192.168.0.105:2379,http://192.168.0.105:4001 \
     -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
     -initial-advertise-peer-urls http://192.168.0.105:2380 \
     -listen-peer-urls http://0.0.0.0:2380 \
     -initial-cluster-token etcd-cluster-1 \
     -initial-cluster etcd0=http://192.168.0.105:2380,etcd1=http://192.168.0.117:2380,etcd2=http://192.168.0.198:2380 \
     -initial-cluster-state new

}

function run2(){

    docker run  -d  -p 4001:4001 -p 2380:2380 -p 2379:2379 --name etcd quay.io/coreos/etcd:v3.3.10 etcd -name etcd1 \
    -advertise-client-urls http://192.168.0.117:2379,http://192.168.0.117:4001 \
     -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
     -initial-advertise-peer-urls http://192.168.0.117:2380 \
     -listen-peer-urls http://0.0.0.0:2380 \
     -initial-cluster-token etcd-cluster-1 \
     -initial-cluster etcd0=http://192.168.0.105:2380,etcd1=http://192.168.0.117:2380,etcd2=http://192.168.0.198:2380\
     -initial-cluster-state new

}

function run3(){
 docker run  -d  -p 4001:4001 -p 2380:2380 -p 2379:2379 --name etcd quay.io/coreos/etcd:v3.3.10 etcd -name etcd2 \
    -advertise-client-urls http://192.168.0.198:2379,http://192.168.0.198:4001 \
     -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
     -initial-advertise-peer-urls http://192.168.0.198:2380 \
     -listen-peer-urls http://0.0.0.0:2380 \
     -initial-cluster-token etcd-cluster-1 \
     -initial-cluster etcd0=http://192.168.0.105:2380,etcd1=http://192.168.0.117:2380,etcd2=http://192.168.0.198:2380\
     -initial-cluster-state new

}

function runWithConfig(){
     docker run  -d  -p 4001:4001 -p 2380:2380 -p 2379:2379 --name etcd quay.io/coreos/etcd:v3.3.10 etcd --config-file = "./etcd.yml"
}


#ps -ef |grep zookeeper 这个就是看zookeeper的启动情况
#grep -v "grep" 是为了去掉查询 grep的那一条
#wc -l 是计数的
COUNT=$(ps -ef |grep zokeeper |grep -v "grep" |wc -l)
echo $COUNT
if [ $COUNT -eq 0 ]; then
        echo NOT RUN
else
        echo is RUN
fi


