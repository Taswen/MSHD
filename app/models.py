from sqlalchemy.orm import Query, query
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import select
from sqlalchemy import text
from app.ext import db
import csv


# 灾情
class Disaster(db.Model):
    # 声明表名
    __tablename__ = 'Disaster'

    Id = db.Column(db.Integer, primary_key=True)
    TypeCode = db.Column(db.Integer)


# 地震
class Earthquake(db.Model):
    # 声明表名

    __tablename__ = 'Earthquake'

    Id = db.Column(db.Integer, primary_key=True)
    OccurrenceTime = db.Column(db.DateTime)
    # str for occurence time
    Str_ot=""
    Longitude = db.Column(db.Float)
    Latitude = db.Column(db.DateTime)
    Depth = db.Column(db.Float)
    Location = db.Column(db.String(100))
    Level = db.Column(db.Float)
    Earthcode = db.Column(db.String(200))

    def __repr__(self):
        return f'<Earthquake> {self.Location}:{self.Level}'

    def enable_print(self):
        self.Str_ot=str(self.OccurrenceTime)
        return self
    
    @classmethod
    def get_max_id(cls):
        query = Earthquake.query.order_by(Earthquake.Id.desc())
        if len(query) == 0:
            return 0
        return query[-1]['Id']

    def readCsv(file):
        start_id = 1
        ref_start_id = 1
        with open("file", "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row['Id'] = str(start_id)
                row['ReferenceId'] = str(ref_start_id)
                obj = Earthquake(row)
                print(obj.gen_sql())
                start_id += 1
                ref_start_id += 1


# print(Earthquake.get_max_id())