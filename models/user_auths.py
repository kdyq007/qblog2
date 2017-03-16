#-*- coding:utf8 -*-
__author__ = 'qiqi'

from application import db
from flask_sqlalchemy import BaseQuery


# class UserAuthsQuery(BaseQuery):
# 	def get(self, uid):
# 		user = self.filter(Users.uid == uid).first()
# 		return user


class UserAuths(db.Model):
    __tablename__ = "user_auths"
    # query_class = UserAuthsQuery

    # EMAIL = 0
    # USERNAME = 1
    # MOBILE = 2
    # WEIXIN = 3
    # QQ = 4
    # WEIBO = 5

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    #唯一ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #用户ID
    auth_type = db.Column(db.Integer, nullable=False)
    identifier = db.Column(db.String(50), nullable=False)
    credential = db.Column(db.String(50), nullable=False)
