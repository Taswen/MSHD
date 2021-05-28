import csv

from app.models import Earthquake

# 疑似废弃
def csv2EarthQuakes(file):
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
