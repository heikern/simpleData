class BaseConfig():
	SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
	SECRET_KEY = 'Just another insecure secret key'
	SQLALCHEMY_TRACK_MODIFICATIONS = True