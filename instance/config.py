import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgres://postgres:@localhost/'
database_name = 'my_diary'


class Config:
    """
    Parent configuration class
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """
    Configurations for development
    """
    DEBUG = True
    DATABASE_URI = postgres_local_base + database_name


class TestingConfig(Config):
    """
    Configurations for testing
    """
    TESTING = True
    DEBUG = True
    DATABASE_URI = postgres_local_base + database_name + '_test'


class ProductionConfig(Config):
    """
    Configurations for production
    """
    DEBUG = False
    TESTING = False


config_environment = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
