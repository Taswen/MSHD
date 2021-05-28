import csv
from dataclasses import dataclass
from typing import Dict


@dataclass
class EarthQuake(object):
    Id: int = 0
    ReferenceId: int = 0
    OccurrenceTime: str = ''
    Level: float = 0.0
    Latitude: float = 0.0
    Longitude: float = 0.0
    Depth: float = 0.0
    Location: str = ''

    def __init__(self, data: Dict):
        super(EarthQuake, self).__init__()
        for key, val in data.items():
            if hasattr(self, key):
                setattr(self, key, type(getattr(self, key))(val))

    def gen_sql(self) -> str:
        keys = ', '.join(self.__dict__.keys())
        values = ', '.join(f"'{value}'" if isinstance(value, str) else f'{value}' for value in self.__dict__.values())
        return f'''
        insert into data.Disaster (Id, TypeCode) values ({self.ReferenceId}, 1);
        insert into data.Earthquake ({keys}) values ({values});'''


if __name__ == '__main__':
    start_id = 1
    ref_start_id = 1
    with open("eqList2021_05_16-2.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['Id'] = str(start_id)
            row['ReferenceId'] = str(ref_start_id)
            obj = EarthQuake(row)
            print(obj.gen_sql())
            start_id += 1
            ref_start_id += 1
