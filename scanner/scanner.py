import logging
import os
import csv
import threading
import time
import schedule
from typing import Dict
from flask_sqlalchemy import SQLAlchemy

from app.models import Disaster, Earthquake


class Scanner(threading.Thread):
    upload_path = '/home/dataput/mshd/upload/'
    scanned_path = '/home/dataput/mshd/scanned/'
    error_path = '/home/dataput/mshd/error/'

    def __init__(self, app):
        super().__init__()
        self.app = app
        app.app_context().push()
        self.session = SQLAlchemy().session

    @classmethod
    def valid_row(cls, row: Dict) -> bool:
        earthquake_minimal_attr = ['Longitude', 'Latitude', 'Level']
        for attr in earthquake_minimal_attr:
            if not row.get(attr, ''):
                return False
        return True

    def start_reading(self):
        print("start reading")
        for filename in os.listdir(self.upload_path):
            try:
                with open(os.path.join(self.upload_path, filename), "r") as file:
                    valid_row = 0
                    reader = csv.DictReader(file)
                    for row in reader:
                        if not self.valid_row(row):
                            logging.warning(f"Ignoring row {row}.")
                            continue
                        disaster = Disaster()
                        disaster.TypeCode = 1
                        self.session.add(disaster)
                        self.session.flush()
                        earthquake = Earthquake(row)
                        earthquake.ReferenceId = disaster.Id
                        self.session.add(earthquake)
                        self.session.commit()
                        valid_row += 1
                    if valid_row == 0:
                        raise Exception('Too little valid rows.')
                os.rename(os.path.join(self.upload_path, filename),
                          os.path.join(self.scanned_path, filename))
            except Exception:
                logging.exception(f"error while processing {filename}:")
                self.session.rollback()
                os.rename(os.path.join(self.upload_path, filename),
                          os.path.join(self.error_path, filename))

    @classmethod
    def init_path(cls) -> None:
        for path in [cls.upload_path, cls.scanned_path, cls.error_path]:
            os.makedirs(path, exist_ok=True)

    def run(self) -> None:
        self.init_path()
        schedule.every(15).seconds.do(self.start_reading)
        while True:
            schedule.run_pending()
            time.sleep(1)
