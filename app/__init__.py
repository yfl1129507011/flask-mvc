#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .controllers.AdminController import admin

app = Flask(__name__)
app.config.from_object('app.common.config')

# 注册蓝图
app.register_blueprint(admin, url_prefix='/admin')

# 引入mysql实例
db = SQLAlchemy(app)

# 自定义404错误页面
@app.errorhandler(404)
def pageNotFound(e):
    return '404错误'

# 自定义500错误页面
@app.errorhandler(500)
def internalServerError(e):
    return '500错误'