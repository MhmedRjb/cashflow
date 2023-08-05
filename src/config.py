class Config(object):
    SECRET_KEY = '123456789'
    DEBUG = True
    # MySQL configuration
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123qweasdzxcSq'
    MYSQL_DATABASE_DB = 'elfateh'
    MYSQL_DATABASE_HOST = 'localhost'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

# ...
