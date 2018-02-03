class Config:
    '''General configuration class'''


class ProdConfig(Config):
    '''Production configuration child class'''


class DevConfig(Config):
    '''Development configuration child class'''
    DEBUG = True
