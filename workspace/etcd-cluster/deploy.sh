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

# 主机清单
HOSTS_FILE=${SCRIPTPATH}/inventories/hosts

function start(){
    ansible-playbook -i ${HOSTS_FILE} -u root ${SCRIPTPATH}/deploy.yml -v
}

start
