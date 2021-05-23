from sqlalchemy import text

from app.models import *


def get_all_earthquakes_data():
    eqs = Earthquake.query.all()
    process_eqs = [e.enable_print() for e in eqs]
    return process_eqs


def get_earthquakes_data(limit=None, offset=None):
    eqs = Earthquake.query.order_by(text("id")).limit(limit).offset(offset).all()
    process_eqs = [e.enable_print() for e in eqs]
    return process_eqs


def get_earthquakes_num():
    return Earthquake.query.count()
