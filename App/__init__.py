from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

dataApp = Flask(__name__)
dataApp.config.from_envvar("APP_CONFIG")
db = SQLAlchemy(dataApp)
from App import views
