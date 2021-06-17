import platform

debug = True
SECRET_KEY = "=kls2kC3bs4ABbc"
if platform.system() == 'Darwin':
    UPLOAD_FOLDER = './upload/'
    SCANNED_FOLDER = './scanned/'
    ERROR_FOLDER = './error/'
else:
    UPLOAD_FOLDER = '/ftp/upload/'
    SCANNED_FOLDER = '/ftp/scanned/'
    ERROR_FOLDER = '/ftp/error/'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://nero:Buptsse18.@47.93.229.92:3306/data?charset=utf8mb4"  #

SQLALCHEMY_TRACK_MODIFICATIONS = True

FTPHOST = "47.93.229.92"
FTPPORT = 21
FTPUSER = "dataput"
FTPPASS = "114514"