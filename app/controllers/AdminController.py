"""
后台控制器
使用蓝图
"""
from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return render_template('admin/index.html')
