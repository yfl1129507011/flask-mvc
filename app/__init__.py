#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.common.config')

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

# 将controllers下的模块全部导入
__all__ = ['controllers']