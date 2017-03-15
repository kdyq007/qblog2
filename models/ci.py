#-*- coding:utf8 -*-
__author__ = 'qiqi'
from application import db
from flask_sqlalchemy import BaseQuery


class CiQuery(BaseQuery):
	def get(self, uid):
		user = self.filter(Ci.uid == uid).first()
		return user

class Ci(db.Model):
    __tablename__ = "ci"
    query_class = CiQuery

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)    #唯一ID
    type = db.Column(db.Integer)
