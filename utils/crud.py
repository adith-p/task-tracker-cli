import json
import time
from . import helpers


def file_writer(
    mode: str,
    json_data: dict,
    desc: str = None,
    task_id: int = 0,
):
    """
    "add", "update", "delete"
    """
    if mode == "add":
        timestamp = helpers.time_stamp()

        json_data[f"tsk{json_data['no_of_total_tasks'] + 1}"] = {
            "description": desc,
            "status": "todo",
            "createdAt": timestamp,
            "modifiedAt": timestamp,
        }
        json_data["no_of_total_tasks"] += 1
        with open("data.json", "w") as file:
            json.dump(json_data, file)

    elif mode == "delete":
        json_data.pop(f"tsk{task_id}")
        with open("data.json", "w") as file:
            json.dump(json_data, file)
