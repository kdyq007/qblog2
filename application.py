#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Qi Qi

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
lm = LoginManager(app)
