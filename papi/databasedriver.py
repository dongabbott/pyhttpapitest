# -*-coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'dongjie'
__data__ = '2015-05-21'
import pymssql
import MySQLdb
import settings
from pyapilog import pyapilog

class sqldriver(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # 执行SQLserver查询
    def exec_mssql(self, sql):
        try:
            conn = pymssql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset="utf8")
            cur = conn.cursor()
            if cur:
                pyapilog().info(u"执行SQL语句|%s|" % sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) == 0:
                    pyapilog().warning(u"没有查询到数据")
                return rows
            else:
                pyapilog().error(u"数据库连接不成功")
            conn.close()
        except Exception, e:
            pyapilog().error(e)

    # 执行Mysql查询
    def exec_mysql(self, sql):
        try:
            conn = MySQLdb.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.database,
                                   )
            cur = conn.cursor()
            if cur:
                pyapilog().info(u"执行SQL语句|%s|" % sql)
                resList = cur.execute(sql)
                return resList
        except Exception, e:
            pyapilog().error(e)

# 执行sql语句返回结果
def execsql(sql):
    config = settings.DATABASE
    driver = config.get("ENGINE")
    host = config.get("HOST")
    port = config.get("PORT")
    user = config.get("USER")
    password = config.get("PWD")
    database = config.get("DATABASE")
    if driver == "MYSQL":
        try:
            sql_result = sqldriver(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            ).exec_mysql(sql)
            return sql_result
        except Exception, e:
            pyapilog().error(e)

    elif driver == "MSSQL":
        try:
            sql_result = sqldriver(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            ).exec_mssql(sql)
            return sql_result
        except Exception, e:
            pyapilog().error(e)
    elif driver == "ORACLE":
        try:
            sql_result = sqldriver(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            ).exec_mssql(sql)
            return sql_result
        except Exception, e:
            pyapilog().error(e)
    else:
        pyapilog().error(u"[%s]数据库配置支持MYSQL、MSSQL、ORACLE" % driver)