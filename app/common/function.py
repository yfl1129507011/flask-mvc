"""
公共函数定义
"""
# MD5加密函数
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()