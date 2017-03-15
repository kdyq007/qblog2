#-*- coding:utf8 -*-
__author__ = 'qiqi'
from application import db
from flask_sqlalchemy import BaseQuery
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
from models.post import Post

class UserQuery(BaseQuery):
	def get(self, uid):
		user = self.filter(User.uid == uid).first()
		return user

class User(db.Model):
    __tablename__ = "user"
    __bind_key__ = "user"
    query_class = UserQuery

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)    #唯一ID
    guid = db.Column(db.String(30),nullable=False) #注册时间+随机数组成的唯一标识文本
    group = db.Column(db.SmallInteger,nullable=False,server_default='2')  #用户组 0：管理员 1：网站编辑 2.作者 3.协作折 4.评论者 5.游客
    password_hash = db.Column(db.String(128), nullable=False, index=True) #加密密码
    cn_name = db.Column(db.String(5), nullable=False,index=True) #中文名
    name = db.Column(db.String(20), nullable=False, index=True)   #帐号
    email = db.Column(db.String(50), nullable=False)  #邮箱
    homepage = db.Column(db.String(50))   #个人主页
    mobile = db.Column(db.String(11)) #手机号码
    description = db.Column(db.String(200))   #个人说明
    ip = db.Column(db.String(15),nullable=False)  #上次登陆IP
    old_password = db.Column(db.Text)  #旧密码
    status = db.Column(db.SmallInteger,nullable=False,server_default='0')  #帐号状态 0:正常 1:禁用 2.审核
    created = db.Column(db.DateTime, nullable=False,server_default='0000-00-00 00:00:00')  #注册账号时间
    posttime = db.Column(db.DateTime,nullable=False,server_default='0000-00-00 00:00:00')  #最后发表时间
    updated = db.Column(db.DateTime, nullable=False,server_default='0000-00-00 00:00:00')  #最后操作时间

    posts = db.relationship(Post,backref='user',lazy='dynamic')   #博文外键

    def __init__(self):
        self.updated = datetime.datetime.now()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash.encode('utf-8'),password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.name)