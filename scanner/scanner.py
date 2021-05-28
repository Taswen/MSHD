import logging
import os
import threading
import time
import schedule

from flask_sqlalchemy import SQLAlchemy

from app.config.settings import UPLOAD_FOLDER, SCANNED_FOLDER, ERROR_FOLDER
from app.models import Earthquake

from scanner.validator.earthquake_validator import EarthquakeValidator
from scanner.converter.to_earthquake import *
from scanner.encoder.encode_eq import eqEncode


logger = logging.Logger("Scanner")


def move(src_path: str, src_filename: str, dst_path: str, dst_filename: str):
    os.makedirs(dst_path, exist_ok=True)
    os.rename(os.path.join(src_path, src_filename),
              os.path.join(dst_path, dst_filename))


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
        logger.info("start reading")
        for filename in os.listdir(UPLOAD_FOLDER):
            try:

                ext_name_split = filename.rsplit('.', maxsplit=1)
                ext_name = ext_name_split[1] if len(ext_name_split) == 2 else ''
                # type check
                if ext_name not in self.type_func_map.keys():
                    if ext_name in ['png', 'jpg', 'jpeg']:
                        continue
                    raise TypeError('Not a accepted file type')

                func = self.type_func_map[ext_name]
                valid_disaster_map = {}
                disaster_list = func(os.path.join(UPLOAD_FOLDER, filename))
                for disaster_dict in disaster_list:
                    if not self.validator.validate(disaster_dict):
                        logger.warning(f"Ignoring row {disaster_dict}.")
                        continue
                    earthquake = Earthquake(disaster_dict)
                    # add source
                    earthquake.Source = filename
                    # encode
                    eqCode = eqEncode("中国",(earthquake.Latitude,earthquake.Longitude),earthquake.OccurrenceTime,earthquake.Level)
                    earthquake.EarthquakeEncode = eqCode
                    
                    self.session.add(earthquake)
                    self.session.flush()
                    valid_disaster_map[earthquake.Id] = disaster_dict
                if len(valid_disaster_map) == 0:
                    raise Exception('No valid rows.')

                type_code = int(list(valid_disaster_map.values())[0]['TypeCode'])
                output_path = os.path.join(SCANNED_FOLDER,
                                           disaster_info_class.get(type_code // 10, 'other'),
                                           disaster_info_subclass.get(type_code, 'other'))
                move(UPLOAD_FOLDER, filename, output_path, filename)

                for disaster_id, disaster_dict in valid_disaster_map.items():
                    for i, image in enumerate(disaster_dict.get('Images', [])):
                        try:
                            image_ext_name = image.rsplit('.', maxsplit=1)[1]
                            move(UPLOAD_FOLDER, image,
                                 os.path.join(output_path, 'images'), f'{disaster_id}_{i}.{image_ext_name}')
                        except Exception:
                            logger.error(f'Image {image} not found.')

                self.session.commit()
                logger.info(f'finished processing {filename}.')
            except Exception:
                logger.exception(f"error while processing {filename}:")
                self.session.rollback()
                move(UPLOAD_FOLDER, filename, ERROR_FOLDER, filename)

    @classmethod
    def init_path(cls) -> None:
        print("Init....")
        for path in [ERROR_FOLDER, UPLOAD_FOLDER, SCANNED_FOLDER]:
            os.makedirs(path, exist_ok=True)
            print(os.path.abspath(path))
        print("Init Done")

    def run(self) -> None:
        self.init_path()
        schedule.every(15).seconds.do(self.start_reading)
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
