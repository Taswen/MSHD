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

def readCsv(file):
    start_id = Earthquake.get_max_id()
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