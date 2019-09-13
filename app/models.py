
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import  login_manager
class User(UserMixin,db.Model):
   """用户"""
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), unique=True, index=True)
   password_hash = db.Column(db.String(128))  # 加密的密码
   email = db.Column(db.String(64),unique=True,index=True)

   @property
   def password(self):
       raise AttributeError('password is not a readable attribute')

   @password.setter
   def password(self, password):
       #generate_password_hash(password,method=pbkdf2:sha1,salt_length=8):密码加密的散列值。
       self.password_hash = generate_password_hash(password)

   def verify_password(self, password):
       #check_password_hash(hash, password) :密码散列值和用户输入的密码是否匹配.
       return check_password_hash(self.password_hash, password)

   def __repr__(self):
       return '<User % r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))