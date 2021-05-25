import logging
import os
import csv
import threading
import time
import schedule
import json
from typing import Dict, List
from flask_sqlalchemy import SQLAlchemy

from app.models import Disaster, Earthquake
from app.config.settings import UPLOAD_FOLDER, SCANNED_FOLDER, ERROR_FOLDER
from validator.earthquake_validator import EarthquakeValidator


def json_reader(path: str) -> List[Dict]:
    with open(path, "r") as file:
        return json.loads(''.join(file.readlines()))['disasters']


def csv_reader(path: str) -> List[Dict]:
    with open(path, "r") as file:
        res = []
        reader = csv.DictReader(file)
        for row in reader:
            res.append(row)
        return res


class Scanner(threading.Thread):
    def __init__(self, app):
        super().__init__()
        self.app = app
        app.app_context().push()
        self.session = SQLAlchemy().session
        self.type_func_map = {
            'csv': csv_reader,
            'json': json_reader,
        }
        self.validator = EarthquakeValidator()

    def start_reading(self):
        print("start reading")
        for filename in os.listdir(UPLOAD_FOLDER):
            try:
                ext_name = filename.rsplit('.', maxsplit=1)
                if len(ext_name) < 2 or ext_name[1] not in self.type_func_map:
                    raise TypeError('Not a accepted file type')
                func = self.type_func_map[ext_name[1]]
                disaster_list = func(os.path.join(UPLOAD_FOLDER, filename))
                valid_row_count = 0
                for disaster_dict in disaster_list:
                    if not self.validator.validate(disaster_dict):
                        logging.warning(f"Ignoring row {disaster_dict}.")
                        continue
                    disaster = Disaster()
                    disaster.TypeCode = 1
                    self.session.add(disaster)
                    self.session.flush()
                    earthquake = Earthquake(disaster_dict)
                    earthquake.ReferenceId = disaster.Id
                    self.session.add(earthquake)
                    valid_row_count += 1
                if valid_row_count == 0:
                    raise Exception('Too little valid rows.')
                self.session.commit()
                os.rename(os.path.join(UPLOAD_FOLDER, filename),
                          os.path.join(SCANNED_FOLDER, filename))
            except Exception:
                logging.exception(f"error while processing {filename}:")
                self.session.rollback()
                os.rename(os.path.join(UPLOAD_FOLDER, filename),
                          os.path.join(ERROR_FOLDER, filename))

    @classmethod
    def init_path(cls) -> None:
        for path in [ERROR_FOLDER, UPLOAD_FOLDER, SCANNED_FOLDER]:
            os.makedirs(path, exist_ok=True)

    def run(self) -> None:
        self.init_path()
        schedule.every(15).seconds.do(self.start_reading)
        while True:
            schedule.run_pending()
            time.sleep(1)
