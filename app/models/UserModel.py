from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(16), unique=True)
    mobile = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(128), nullable=False)
    reg_time = db.Column(db.Date)

    def __init__(self, nickname, mobile, password):
        self.nickname = nickname
        self.mobile = mobile
        self.passwordHash = password
        from time import strftime
        self.reg_time = strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return '<User %r>' % self.nickname

    @property
    def passwordHash(self):
        raise AttributeError('password is not a readable attribute')

    @passwordHash.setter
    def passwordHash(self, password):
        from werkzeug.security import generate_password_hash
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)