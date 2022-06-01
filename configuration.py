import os

DB_USER = os.getenv('DB_USER', '')
DB_PASS = os.getenv('DB_PASS', '')
DB_PORT = 3306
DB_NAME = 'bib'
DB_HOST = '127.0.0.1'


class BaseConfiguration:
    DEBUG = True
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
    )
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MINIFY_HTML = True


class ProductionConfiguration(BaseConfiguration):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
    )

    DEBUG_TB_ENABLED = False
    MINIFY_HTML = True