import sys
from utils import crud
import pathlib, json
from utils import helpers


def main():
    """Processes command-line arguments for task management operations:

    **Task Modification:**
    - `add <description>`: Adds a new task with the given description.
    - `delete <task_id>`: Deletes the task with the specified ID.
    - `update <task_id> <description>`: Updates the description of the task with the specified ID.

    **Task Listing:**
    - `list`: Lists all tasks.
    - `list done|in-progress|todo`: Lists tasks with the specified status.

    **Task Status Update:**
    - `mark-done <task_id>`: Marks the task with the specified ID as done.
    - `mark-in-progress <task_id>`: Marks the task with the specified ID as in-progress.
    """
    json_file = pathlib.Path("data.json")

    if not json_file.exists() or helpers.is_file_empty():
        data = {"no_of_total_tasks": 0}
        with open("data.json", "a+") as file:
            json.dump(data, file)

    json_data = helpers.json_data()

    if len(sys.argv) == 2:
        if sys.argv[1] == "list":
            for i in range(1, json_data["no_of_total_tasks"]):
                print(json_data[f"tsk{i}"])

    if len(sys.argv) == 3:

        if sys.argv[1] == "add":
            crud.task_writer(json_data=json_data, mode=sys.argv[1], desc=sys.argv[2])
        elif sys.argv[1] == "delete":
            crud.task_writer(json_data=json_data, mode=sys.argv[1], task_id=sys.argv[2])
        elif sys.argv[1] in ["mark-done", "mark-in-progress"]:
            crud.task_writer(json_data=json_data, mode=sys.argv[1], task_id=sys.argv[2])
        elif sys.argv[1] == "list" and sys.argv[2] in ["done", "todo", "in-progress"]:
            crud.list_task(mode=sys.argv[2], json_data=json_data)

    if len(sys.argv) == 4:
        if sys.argv[1] == "update":
            crud.task_writer(
                json_data=json_data,
                mode=sys.argv[1],
                task_id=sys.argv[2],
                desc=sys.argv[3],
            )


if __name__ == "__main__":
    main()
