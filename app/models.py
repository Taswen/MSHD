from importlib.machinery import SourceFileLoader
from typing import Dict
from enum import Enum

from app.ext import db
import csv


class DisasterTypeCode(Enum):
    UNKNOWN = 0
    EARTHQUAKE = 1


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
    Str_ot = ""
    Longitude = db.Column(db.Float)
    Latitude = db.Column(db.DateTime)
    Depth = db.Column(db.Float)
    Location = db.Column(db.String(100))
    Level = db.Column(db.Float)
    EarthquakeEncode = db.Column(db.String(200))
    ReferenceId = db.Column(db.Integer, db.ForeignKey('Disaster.Id'))
    ReportingUnit = db.Column(db.String(100))
    Source = db.Column(db.String(100))

    def __repr__(self):
        return f'<Earthquake> {self.Location}:{self.Level}'

    def enable_print(self):
        self.Str_ot = str(self.OccurrenceTime)
        return self
    
    @classmethod
    def get_max_id(cls):
        query = Earthquake.query.order_by(Earthquake.Id.desc())
        if len(query) == 0:
            return 0
        return query[-1]['Id']

    def __init__(self, data: Dict):
        for key, val in data.items():
            if hasattr(self, key):
                # setattr(self, key, type(getattr(self, key))(val))
                setattr(self, key, val)
