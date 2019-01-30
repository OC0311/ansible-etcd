#!/bin/bash
# Created by martin on 24/01/2019

set -e

pushd $(dirname $0) > /dev/null
SCRIPTPATH=$(pwd -P)
popd > /dev/null
SCRIPTFILE=$(basename $0)

export PYTHONPATH=${SCRIPTPATH}:${PYTHONPATH}


function log() {
    echo "================================================================================"
    echo "$(date +'%Y-%m-%d %H:%M:%S%z') [INFO] - $@"
    echo ""
}

function err() {
    echo "================================================================================"
    echo "$(date +'%Y-%m-%d %H:%M:%S%z') [ERRO] - $@" >&2
}

# 主机清单
HOSTS_FILE=${SCRIPTPATH}/ansible-scaring/inventories/hosts
# 工作空间目录
WORKSPACE=${SCRIPTPATH}/workspace

function start(){
    echo "-------"
    echo ${SCRIPTPATH}

    # 生成工作目录
    log "==>>【准备】1. 创建工作目录 ${WORKSPACE}..."
    rm -rf ${WORKSPACE}
    mkdir -p ${WORKSPACE}

    log "==>>【准备】2. 复制ansible部署脚本..."
    cp -r ${SCRIPTPATH}/etcd-cluster ${WORKSPACE}/

    log "==>>【准备】3. 生成hosts文件要以及节点配置文件..."
    python ${SCRIPTPATH}/src/main.py --config=${SCRIPTPATH}/cfg/${CONFIG}

#    # 执行部署脚本
    log "==>>【准备】4. 集群部署..."
    ${WORKSPACE}/etcd-cluster/deploy.sh
}

function showUsage() {
    echo -e ""
    echo -e "${SCRIPTFILE} [-h] -c <config file>"
    echo -e ""
    echo -e "    -h : Show this message"
    echo -e "    -c : config file"
    echo -e ""
    echo -e "Sample Usage:"
    echo -e ""
    echo -e "    ${SCRIPTFILE} -c config.yml"
    echo -e ""
}

while getopts 'hc:' ARG; do
    case "${ARG}" in
        h) showUsage; exit ;;
        c) CONFIG=${OPTARG} ;;
    esac
done

if [ !-f ${CONFIG} ]; then
    err "配置文件不存在!"
    exit 1
fi

start


