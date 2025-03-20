# task-tracker-cli
project url - https://roadmap.sh/projects/task-tracker

A simple command-line interface (CLI) application to manage your tasks. This application allows you to add, update, delete, mark, and list your tasks, storing the data in a `data.json` file.

## Features

* **Add Tasks:** Create new tasks with a description.
* **Update Tasks:** Modify the description of existing tasks.
* **Delete Tasks:** Remove tasks from your list.
* **Mark Task Status:** Change the status of a task to "in progress" or "done".
* **List All Tasks:** View all tasks in your tracker.
* **List Tasks by Status:** Filter and view tasks that are "done", "not done" (including "todo" and "in-progress"), or specifically "in progress".

## Getting Started

1.  Make sure you have Python 3 installed on your system.
2.  Open your terminal or command prompt and navigate to the project's root directory.

## Usage

The application is run using the following syntax:

```bash
python main.py <command> [arguments]

task-tracker-cli/
├── utils/
│   ├── __init__.py
│   ├── crud.py
│   └── helpers.py
├── .gitignore
├── README.md
├── data.json
└── main.py
