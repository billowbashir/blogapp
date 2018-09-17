import os

class Config:

    '''
    class config

    '''

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    SECRET_KEY=os.environ.get("SECRET_KEY")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bashir:bashiir@localhost/blog_test'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://bashir:bashiir@localhost/blog'
    SECRET_KEY=os.environ.get("SECRET_KEY")
    DEBUG = True

config_options = {
'development':DevConfig,
'test':TestConfig,
'production':ProdConfig
}
