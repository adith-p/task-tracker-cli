import os
import json
from datetime import datetime


def time_stamp():
    """Returns the current date and time in ISO format."""
    return datetime.now().isoformat()


def json_data():
    """Reads and parses JSON data from the 'data.json' file.

    Returns:
        dict: The JSON data loaded from 'data.json'.
    """
    with open("data.json", "r") as file:
        return json.load(file)


def is_file_empty():
    """Checks if the 'data.json' file is empty.

    Returns:
        bool: True if the file size is 0 or less, False otherwise.
    """
    return os.path.getsize("data.json") <= 0
