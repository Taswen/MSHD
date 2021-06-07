from typing import Dict


class EarthquakeValidator(object):
    def validate(self, data: Dict) -> bool:
        earthquake_minimal_attr = ['Longitude', 'Latitude', 'Level', 'OccurrenceTime']
        for attr in earthquake_minimal_attr:
            if not data.get(attr, ''):
                return False
        return True
