#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Qi Qi

from application import app
from application import db
from flask_script import Manager
from flask_script import Server

manager = Manager(app)
manager.add_command('runserver', Server(host=app.config.get('HOST', '127.0.0.1'), port=app.config.get('PORT', 5000),
                                        use_debugger=app.config.get('DEBUG', False)))


@manager.command
def create_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app.run()
