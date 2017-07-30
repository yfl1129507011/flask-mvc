from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(16), unique=True)
    mobile = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(32), nullable=False)
    reg_time = db.Column(db.Date)

    def __init__(self, nickname, mobile, password, reg_time):
        self.nickname = nickname
        self.mobile = mobile
        self.password = password
        self.reg_time = reg_time

    def __repr__(self):
        return '<User %r>' % self.nickname