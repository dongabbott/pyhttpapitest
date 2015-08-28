# -*-coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'dongjie'
__data__ = '2015-05-20'


'''
    配置系统相关的参数,提供全局的相关配置
'''
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置测试目录,以下配置为根目录下case/account, 如果需要配置多个测试目录在下面列表中增加一条
CASE_SUITE = (

    os.path.join(os.path.dirname(__file__), 'case', 'account').replace(
        '\\', '/'),
    os.path.join(os.path.dirname(__file__), 'case', 'maps').replace('\\', '/'),
)

# 日志路径配置，以下配置为项目根目录下的log文件目录
LOGPATH = os.path.join(os.path.dirname(__file__), 'log',).replace('\\', '/')
# 日志输出等级配置 log等级,1:notset 2:debug  3:info 4:warning 5:error 6:critical
LOGLEVEL = 2

#Api测试地址
SERVER = 'webapi.yilule.com:5580'

# 数据库配置，支持MYSQL、MSSQL、ORACLE
DATABASE = {
    "ENGINE": "MSSQL",
    "HOST": "yiluletest.sqlserver.rds.aliyuncs.com",
    "PORT": 3433,
    "USER": "topwysa",
    "PWD": "sqlQ_1",
    "DATABASE": "yiluletest1"
}

