import csv
import json
import logging
import os
import threading
import time
from typing import Dict, List

import schedule
from flask_sqlalchemy import SQLAlchemy

from app.app import app
from app.config.settings import UPLOAD_FOLDER, SCANNED_FOLDER, ERROR_FOLDER
from app.models import Earthquake, HouseDamaged, InjuredStatistics

logging.basicConfig(level=logging.DEBUG)
logger = app.logger
move_queue = {}


def json_reader(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as file:
        return json.loads(''.join(file.readlines()))['disasters']


def csv_reader(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as file:
        res = []
        reader = csv.DictReader(file)
        for row in reader:
            res.append(row)
        return res


def move(src_path: str, src_filename: str, dst_path: str, dst_filename: str):
    global move_queue
    os.makedirs(dst_path, exist_ok=True)
    src_full_path = os.path.join(src_path, src_filename)
    dst_full_path = os.path.join(dst_path, dst_filename)
    if os.path.exists(src_full_path):
        os.rename(src_full_path, dst_full_path)
    else:
        move_queue[src_full_path] = dst_full_path


def try_move_from_queue():
    global move_queue
    for src, dst in list(move_queue.items()):
        if os.path.exists(src):
            os.rename(src, dst)
            del move_queue[src]


class Scanner(threading.Thread):
    def __init__(self):
        super().__init__()
        self.app = app
        app.app_context().push()
        self.session = SQLAlchemy().session
        self.type_func_map = {
            'csv': csv_reader,
            'json': json_reader,
        }

    def start_reading(self):
        logger.info("start reading")
        for filename in os.listdir(UPLOAD_FOLDER):
            try:
                # file type check
                ext_name_split = filename.rsplit('.', maxsplit=1)
                ext_name = ext_name_split[1] if len(ext_name_split) == 2 else ''
                if ext_name not in self.type_func_map.keys():
                    if ext_name in ['png', 'jpg', 'jpeg']:
                        continue
                    raise TypeError('Not a accepted file type')

                func = self.type_func_map[ext_name]
                valid_disaster_map = {}
                disaster_list = func(os.path.join(UPLOAD_FOLDER, filename))

                # save to database
                for disaster_dict in disaster_list:
                    type_code = disaster_dict['TypeCode']
                    if type_code // 10 == 2:
                        disaster = HouseDamaged(disaster_dict)
                    elif type_code // 10 == 1:
                        disaster = InjuredStatistics(disaster_dict)
                    else:
                        disaster = Earthquake(disaster_dict)
                        disaster.Source = filename  # add source
                    if not disaster.validate():
                        continue
                    self.session.add(disaster)
                    self.session.flush()
                    valid_disaster_map[disaster.Id] = disaster_dict

                # move input files to SCANNED_FOLDER
                type_code = int(list(valid_disaster_map.values())[0]['TypeCode'])
                output_path = os.path.join(SCANNED_FOLDER,
                                           disaster_info_class.get(type_code // 10, 'other'),
                                           disaster_info_subclass.get(type_code, 'other'))
                move(UPLOAD_FOLDER, filename, output_path, filename)
                for disaster_id, disaster_dict in valid_disaster_map.items():
                    for i, image in enumerate(disaster_dict.get('Images', [])):
                        image_ext_name = image.rsplit('.', maxsplit=1)[1]
                        move(UPLOAD_FOLDER, image,
                             os.path.join(output_path, 'images'), f'{disaster_id}_{i}.{image_ext_name}')

                self.session.commit()
                logger.info(f'finished processing {filename}.')

            except Exception:
                logger.exception(f"error while processing {filename}:")
                self.session.rollback()
                move(UPLOAD_FOLDER, filename, ERROR_FOLDER, filename)

    @classmethod
    def init_path(cls) -> None:
        logger.debug("Init....")
        for path in [ERROR_FOLDER, UPLOAD_FOLDER, SCANNED_FOLDER]:
            os.makedirs(path, exist_ok=True)
            logger.debug(os.path.abspath(path))
        logger.debug("Init Done")

    def run(self) -> None:
        self.init_path()
        schedule.every(15).seconds.do(self.start_reading)
        schedule.every(15).seconds.do(try_move_from_queue)
        while True:
            schedule.run_pending()
            time.sleep(1)


disaster_info_class = {
    1: '人员伤亡及失踪',
    2: '房屋破坏',
    3: '生命线工程灾情',
    4: '次生灾害',
    5: '震情',
}

disaster_info_subclass = {
    11: 'DeathStatistics',
    12: 'InjuredStatistics',
    13: 'MissingStatistic',
    21: 'CivilStructure',
    22: 'BrickWoodStructure',
    23: 'MasonryStructure',
    24: 'FrameworkStructure',
    25: 'OtherStructure',
    31: 'TrafficDisaster',
    32: 'WaterDisaster',
    33: 'OilDisaster',
    34: 'GasDisaster',
    35: 'PowerDisaster',
    36: 'CommDisaster',
    37: 'IrrigationDisaster',
    41: 'CollapseRecord',
    42: 'LandslideRecord',
    43: 'DebrisRecord',
    44: 'KarstRecord',
    45: 'CrackRecord',
    46: 'SettlementRecord',
    47: 'OtherRecord',
    51: 'DisasterInfo',
    52: 'DisasterPrediction',
}
