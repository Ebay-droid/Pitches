import os

class Config:

    SECRET_KEY ="just a key"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ebay:qwerty@localhost/pitches'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}