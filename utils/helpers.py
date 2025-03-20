import os
import json
import time
from datetime import datetime


def time_stamp():
    return datetime.now().isoformat()


def json_data():
    with open("data.json", "r") as file:
        return json.load(file)


def is_file_empty():

    return os.path.getsize("data.json") <= 0
