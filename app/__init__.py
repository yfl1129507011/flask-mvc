#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.common.config')

# 引入mysql实例
db = SQLAlchemy(app)

# 将controllers下的模块全部导入
__all__ = ['controllers']