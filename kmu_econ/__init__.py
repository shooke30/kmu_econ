# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import pymysql
#pymysql.install_as_MySQLdb()
#import MySQLdb


# 得到Flask 类的实例对象 app
app = Flask(__name__)


#import  os
#print os.environ.keys()
#print os.environ.get('FLASKR_SETTINGS')
#加载配置文件内容
app.config.from_object('kmu_econ.setting')     #模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径

#创建数据库对象
db = SQLAlchemy(app)

#只有在app对象之后声明，用于导入model否则无法创建表
from kmu_econ.model import User,Category
from kmu_econ.controller import kmu_econ_manage