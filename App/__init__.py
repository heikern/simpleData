from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


dataApp = Flask(__name__)
#dataApp.config.from_object('config.DevelopmentConfig')
dataApp.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
print os.environ['DATABASE_URL']
db = SQLAlchemy(dataApp)
from App import views
