from app.ext import db


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
