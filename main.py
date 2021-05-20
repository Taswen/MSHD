from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 加载配置
app.config.from_pyfile("config/config.py")

db = SQLAlchemy(app)

# 灾情
class Disaster(db.Model):
    #声明表名
    __tablename__ = 'Disaster'

    #建立字段函数
    Id = db.Column(db.Int,primary_key=True)
    TypeCode = db.Column(db.Int)


# 地震
class Earthquake(db.Model):

    #声明表名

    __tablename__ = 'Earthquake'
    
    #建立字段函数

    Id = db.Column(db.Int,primary_key=True)
    OccurrenceTime = db.Column(db.DataTime)
    Longitude = db.Column(db.Double)
    Latitude = db.Column(db.Double)
    Depth = db.Column(db.Double)
    Location = db.Column(db.Double)
    OccurrenceTime = db.Column(db.DataTime)
    OccurrenceTime = db.Column(db.DataTime)
    name = db.Column(db.String(200))

if __name__ == '__main__':
    app.run()