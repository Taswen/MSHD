# 开启调试
DEBUG=True
# 上传文件
UPLOAD_FOLDER='uploadFiles/'

# 数据库配置
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://nero:nero@47.93.229.92:3306/data?charset=utf8"#


SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 指定配置，用来省略提交操作