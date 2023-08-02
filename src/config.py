# config.py
class Config(object):
    SECRET_KEY = '123456789'
    DEBUG = True
    # Database connection details
    DB_USERNAME = 'root'
    DB_PASSWORD = '123qweasdzxcSq'
    DB_HOSTNAME = 'localhost'
    DB_DATABASE = 'elfateh'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
