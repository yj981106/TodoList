from flask import  Blueprint
# 'auth'是蓝图的名称
# __name__是蓝图所在路径
auth =Blueprint('auth',__name__)
from . import views