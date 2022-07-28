# -*- coding: utf-8 -*-
__version__ = '0.1'

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_session import Session


""" App """
app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'super-secret'
toolbar = DebugToolbarExtension(app)

jwt = JWTManager(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
Session(app)

from project.controllers.web import *
from project.jwt import *
from project.controllers.api import *
