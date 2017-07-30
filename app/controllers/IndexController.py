from app import app
from flask import render_template, request, redirect, url_for, session
from app.models.UserModel import User, db
from app.common.function import md5
import json, time

# 首页
@app.route('/')
def index():
    if 'mobile' not in session:
        return redirect(url_for('login'))
    users = User.query.all()
    return render_template('home/index.html', mobile=session['mobile'], users=users)


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = {}
        mobile = request.form.get('mobile', None)
        password = request.form.get('password', None)
        if not mobile or not password:
            data['status'] = 404
            data['info'] = '手机、密码不能为空'
            return json.dumps(data)
        info = User.query.filter_by(mobile=mobile).first()
        if info == None:
            data['status'] = 404
            data['info'] = '账号错误'
            return json.dumps(data)
        if info.password != md5(password):
            data['status'] = 404
            data['info'] = '密码错误'
            return json.dumps(data)
        session['mobile'] = mobile
        data['status'] = 200
        data['url'] = url_for('index')
        return json.dumps(data)
    else:
        if 'mobile' in session:
            return redirect(url_for('index'))
        return render_template('home/login.html')

# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {}
        nickname = request.form.get('nickname', None)
        mobile = request.form.get('mobile', None)
        password = request.form.get('password', None)
        rePassword = request.form.get('rePassword', None)
        if not nickname or not mobile or not password:
            data['status'] = 404
            data['info'] = '昵称、手机、密码不能为空'
            return json.dumps(data)
        if password != rePassword:
            data['status'] = 404
            data['info'] = '密码不一致'
            return json.dumps(data)
        reg_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user = User(nickname, mobile, md5(password), reg_time)
        db.session.add(user)
        db.session.commit()
        return json.dumps({'status': 200, 'url': url_for('login')})
    else:
        if 'mobile' in session:
            return redirect(url_for('index'))
        return render_template('home/register.html')

# 用户编辑
@app.route('/user/edit/<int:id>')
def userEdit(id):
    if 'mobile' not in session:
        return redirect(url_for('login'))
    info = User.query.get(id)
    # 更新
    info.nickname += '_FL'
    db.session.commit()
    return json.dumps({'id': info.id, 'nickname': info.nickname, 'mobile': info.mobile})

# 删除用户
@app.route('/user/del/<int:id>')
def userDel(id):
    if 'mobile' not in session:
        return redirect(url_for('login'))
    res = User.query.filter_by(id=id).delete()
    print(res)
    return redirect(url_for('index'))

# 退出
@app.route('/logout')
def logout():
    session.pop('mobile', None)
    return redirect(url_for('login'))