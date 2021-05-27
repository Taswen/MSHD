import json,csv
from typing import Dict, List

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