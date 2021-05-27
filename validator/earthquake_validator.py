from typing import Dict

from validator.base_validator import Validator


class EarthquakeValidator(Validator):
    def validate(self, data: Dict) -> bool:
        earthquake_minimal_attr = ['Longitude', 'Latitude', 'Level']
        for attr in earthquake_minimal_attr:
            if not data.get(attr, ''):
                return False
        return True
