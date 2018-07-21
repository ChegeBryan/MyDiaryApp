import os


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


class TestingConfig(Config):
    """
    Configurations for testing
    """
    TESTING = True
    DEBUG = True


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
