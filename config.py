import os

class BaseConfig():
	#SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SECRET_KEY = '\x98k\xa4\xa4:\xedzO0\x8a\xc9X\x93\xc9\x94o*p\x9atum)\xb5'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	DEBUG = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductingConfig(BaseConfig):
	DEBUG = False
