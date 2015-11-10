from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


dataApp = Flask(__name__)
#dataApp.config.from_object('config.DevelopmentConfig')
dataApp.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(dataApp)
from App import views
