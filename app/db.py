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

def get_one_earthquake_by_id(id):
    return Earthquake.query.get(id).enable_print()


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


def get_all_HouseDamaged_data():
    hds = HouseDamaged.query.all()
    house_damaged = [hd.enable_print() for hd in hds]
    return house_damaged


def get_all_InjuredStatistics_data():
    ists = InjuredStatistics.query.all()
    injured_data = [ist.enable_print() for ist in ists]
    return injured_data


def delete_one_HouseDamaged_by_id(id):
    house_damaged = HouseDamaged.query.filter(HouseDamaged.Id == id).first()
    db.session.delete(house_damaged)
    db.session.commit()


def delete_one_InjuredStatistics_by_id(id):
    injured_data = InjuredStatistics.query.filter(InjuredStatistics.Id == id).first()
    db.session.delete(injured_data)
    db.session.commit()