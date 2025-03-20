import json

from . import helpers


def task_writer(
    mode: str,
    json_data: dict,
    desc: str = None,
    task_id: int = 0,
):
    """Manages the creation, deletion, and status updates of tasks in the task tracker data.

    Args:
        mode (str): The operation to perform. Valid values are:
            - "add": Adds a new task. Requires the 'desc' argument.
            - "delete": Deletes an existing task. Requires the 'task_id' argument.
            - "mark-in-progress": Marks an existing task as 'in-progress'. Requires the 'task_id' argument.
            - "mark-done": Marks an existing task as 'done'. Requires the 'task_id' argument.
        json_data (dict): A dictionary containing the task tracker data, typically loaded from 'data.json'.
        desc (str, optional): The description of the new task to be added. Required when mode is "add". Defaults to None.
        task_id (int, optional): The ID of the task to be deleted or updated. Required when mode is "delete", "mark-in-progress", or "mark-done". Defaults to 0.

    Raises:
        KeyError: If 'task_id' is invalid for 'delete', 'mark-in-progress', or 'mark-done' modes.

    Returns:
        None: This function modifies the 'json_data' dictionary in place and writes the updated data to the 'data.json' file.
    """
    if mode == "add":
        timestamp = helpers.time_stamp()

        json_data[f"tsk{json_data['no_of_total_tasks'] + 1}"] = {
            "task_id": json_data["no_of_total_tasks"] + 1,
            "description": desc,
            "status": "todo",
            "createdAt": timestamp,
            "modifiedAt": timestamp,
        }
        json_data["no_of_total_tasks"] += 1
        with open("data.json", "w") as file:
            json.dump(json_data, file)

        print(f"Output: Task added successfully (ID: {json_data["no_of_total_tasks"]})")

    elif mode == "delete":
        json_data.pop(f"tsk{task_id}")
        json_data["no_of_total_tasks"] -= 1

        with open("data.json", "w") as file:
            json.dump(json_data, file)

    elif mode in ["mark-in-progress", "mark-done"]:
        if mode == "mark-done":
            json_data[f"tsk{task_id}"]["status"] = "done"
        else:
            json_data[f"tsk{task_id}"]["status"] = "in-progress"

        with open("data.json", "w") as file:
            json.dump(json_data, file)

    elif mode == "update":
        json_data[f"tsk{task_id}"]["description"] = desc
        json_data[f"tsk{task_id}"]["modifiedAt"] = helpers.time_stamp()

        with open("data.json", "w") as file:
            json.dump(json_data, file)


def list_task(mode: str, json_data: dict):
    """Lists tasks from the provided data based on their status.

    Args:
        mode (str): The status to filter tasks by. Valid values are "done", "todo", or "in-progress".
        json_data (dict): A dictionary containing the task data, where keys are task IDs and values are task details (including 'status').

    Returns:
        None: This function prints the details of the tasks that match the specified status to the console.
    """
    if mode in ["done", "todo", "in-progress"]:
        for i in range(1, json_data["no_of_total_tasks"] + 1):
            if json_data[f"tsk{i}"]["status"] == mode:
                print(json_data[f"tsk{i}"])
