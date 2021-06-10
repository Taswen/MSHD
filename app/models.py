from enum import Enum
from typing import Dict

from app.encoder.encode_eq import eq_encode
from app.ext import db


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
                setattr(self, key, val)
        self.EarthquakeEncode = eq_encode("中国", (self.Latitude, self.Longitude), self.OccurrenceTime, self.Level)

    def validate(self) -> bool:
        earthquake_minimal_attr = ['Longitude', 'Latitude', 'Level', 'OccurrenceTime']
        for attr in earthquake_minimal_attr:
            if not getattr(self, attr, ''):
                return False
        return True


class HouseDamaged(db.Model):
    __tablename__ = "HouseDamaged"

    Id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(255))
    Date = db.Column(db.DateTime)
    Location = db.Column(db.String(255))
    BasicallyIntactSquare = db.Column(db.Float)
    Level = db.Column(db.String(255))
    DamagedSquare = db.Column(db.Float)
    DestroyedSquare = db.Column(db.Float)
    ReportingUnit = db.Column(db.String(255))
    EarthquakeId = db.Column(db.Integer, db.ForeignKey("Earthquake.Id"))

    # 一对多关系映射,
    Earthqu = db.relationship("Earthquake", backref="HouseDamageds")

    def enable_print(self):
        self.Str_ot = str(self.Date)
        return self

    def __init__(self, data: Dict):
        for key, val in data.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def validate(self) -> bool:
        earthquake_minimal_attr = ['Location']
        for attr in earthquake_minimal_attr:
            if not getattr(self, attr, ''):
                return False
        return True


class InjuredStatistics(db.Model):
    __tablename__ = "InjuredStatistics"

    Id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.DateTime)
    Location = db.Column(db.String(255))
    DeathNumber = db.Column(db.Integer)
    InjuredNumber = db.Column(db.Integer)
    MissingNumber = db.Column(db.Integer)
    ReportingUnit = db.Column(db.String(255))
    EarthquakeId = db.Column(db.Integer, db.ForeignKey("Earthquake.Id"))

    # 一对多关系映射,
    Earthqu = db.relationship("Earthquake", backref="InjuredStatistics")

    def enable_print(self):
        self.Str_ot = str(self.Date)
        return self

    def __init__(self, data: Dict):
        for key, val in data.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def validate(self) -> bool:
        earthquake_minimal_attr = ['Location']
        for attr in earthquake_minimal_attr:
            if not getattr(self, attr, ''):
                return False
        return True
