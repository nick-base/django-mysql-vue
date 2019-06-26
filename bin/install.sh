#!/bin/bash
. ./bin/base.sh --source-only

if [ "$1" == 'init' ]
then
  # 检查下载安装Anaconda3
  check_conda=$(conda --version | grep "${conda_version}")
  if [ "$check_conda" == "" ]
  then
    echo 'Download Anaconda3...'
    wget "${anaconda_repo_path}${anaconda3_file}"
    sh ${anaconda3_file}
    rm ${anaconda3_file}
  else
    success "Anaconda${conda_version}已存在"
  fi

  # 检查环境变量
  check_path=$(cat ~/.bashrc | grep "anaconda")
  if [ "$check_path" == "" ]
  then
    echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc
  else
    success "Anaconda环境变量中已已存在"
  fi

  # 创建开发环境
  conda create -n $env_name python=$python_version
fi

# 安装Python依赖包
source activate $env_name
pip install -r ${requirements_path}
