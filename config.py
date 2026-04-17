class Config:
    SECRET_KEY = 'your-secret-key'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/prod'
    # Other production configurations here
