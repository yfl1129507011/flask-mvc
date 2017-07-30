# 配置
DEBUG = True  # 设置调试模式
SECRET_KEY = b'_@8a!+<hd>+0(-7%@_'   # 密钥
# mysql配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True