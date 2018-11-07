# _*_ coding: utf-8 _*_

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # session必须要设置key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # 调试模式是否开启
    DEBUG = True
    #Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mysql数据库连接信息,这里改为自己的账号
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/kmu_econ"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#定义了一个config的字典，作为外部调用这些配置的接口
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig,
    'default': DevelopmentConfig
}

