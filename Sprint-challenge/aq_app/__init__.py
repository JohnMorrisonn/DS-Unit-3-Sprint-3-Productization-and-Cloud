from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

DB = SQLAlchemy(APP)

from aq_app import aq_dashboard as aq