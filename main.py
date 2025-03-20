import sys, os
from utils import crud
import pathlib, json
from utils import helpers


def main():
    json_file = pathlib.Path("data.json")

    if not json_file.exists() or helpers.is_file_empty():
        data = {"no_of_total_tasks": 0}
        with open("data.json", "a+") as file:
            json.dump(data, file)

    if len(sys.argv) > 2:
        if sys.argv[1] in ["add", "update", "delete"]:
            crud.file_writer(
                json_data=helpers.json_data(), mode=sys.argv[1], desc=sys.argv[2]
            )


if __name__ == "__main__":
    main()
