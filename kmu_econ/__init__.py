# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
#import pymysql
#pymysql.install_as_MySQLdb()
#import MySQLdb

db=SQLAlchemy()

def create_app(config_name):
    # 得到Flask 类的实例对象 app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #创建数据库对象
    db.init_app(app)

    return app

app = create_app('development')

# 只有在app对象之后声明，用于导入model否则无法创建表
from kmu_econ.models import User, Category
from kmu_econ.views import kmu_econ_manage

