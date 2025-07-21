# 🐛 Bug Reporter CLI

A simple command-line tool to help you track and manage bugs in your project. It allows you to add, update, delete, and store bug reports locally in a JSON file. Built with Python, tested with Pytest, and packaged with Docker for easy use anywhere.

---

## 📦 Features

- Create new bug reports with title, description, and priority
- Assign bugs and update their status
- Delete bugs by ID
- List all bugs
- Save bug data to a local JSON file (`bugs.json`)
- Fully tested with Pytest
- Dockerized for platform-independent use

---

## 📁 Project Structure

```
Bug Reporter CLI/
├── bugs/
│   ├── models.py          # Defines the Bug class
│   └── manager.py         # Handles bug storage and manipulation
├── tests/
│   └── test_manager.py    # Unit tests for core logic
├── bugs.json              # Local storage for bug data
├── cli.py                 # Main CLI script using argparse
├── Dockerfile             # Docker setup for running the app
├── requirements.txt       # Python dependencies
└── README.md              # You're reading it
```

---

## 🚀 Getting Started

### 🔧 1. Clone & Setup Environment

```bash
git clone https://github.com/johnmesfn/Bug-Reporter-CLI.git
cd Bug-Reporter-CLI
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

---

### 🧪 2. Run Tests

```bash
PYTHONPATH=. pytest
```

**Arguments:**
- `--title`: The title of the bug (required).
- `--description`: A detailed description of the bug (required).
- `--priority`: The priority of the bug (e.g., `low`, `medium`, `high`). Defaults to `low`.
- `--assigned-to`: The person the bug is assigned to.

### List all bugs

To see all the bugs that have been reported, use the `list` command.

```bash
python cli.py list
```

### Update an existing bug

To update a bug, use the `update` command with the bug's ID and the fields you want to change.

```bash
python cli.py update 1 --status "in_progress" --priority "critical"
```

### Delete a bug

To remove a bug, use the `delete` command with the bug's ID.

```bash
python cli.py delete 1
```