# 🐛 Bug Reporter CLI

A simple command-line tool to help you track and manage bugs in your project. You can add, update, delete, comment on, and list bugs stored locally in a JSON file. Built with Python, tested with Pytest, and Dockerized for easy cross-platform use.

---

## 📦 Features

* Create new bug reports with title, description, priority, and assignee
* Update bug details and status
* Add comments to bugs
* Delete bugs by ID
* List bugs with optional filtering by status or priority
* Persistent storage in a local JSON file (`bugs.json`)
* Fully tested with Pytest
* Packaged with Docker for easy deployment

---

## 📁 Project Structure

```
Bug Reporter CLI/
├── bugs/
│   ├── models.py          # Bug class definition
│   └── manager.py         # Core bug operations (load, save, add, update, delete)
├── tests/
│   └── test_manager.py    # Unit tests for manager module
├── bugs.json              # JSON file storing bug data
├── cli.py                 # Main CLI script using argparse
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🚀 Getting Started

### 1. Clone & Setup Environment

```bash
git clone https://github.com/johnmesfn/Bug-Reporter-CLI.git
cd Bug-Reporter-CLI
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. Run Tests

```bash
PYTHONPATH=. pytest
```

---

## 💻 Usage

Run the CLI tool with Python:

```bash
python cli.py <command> [options]
```

---

### Commands

#### Add a new bug

```bash
python cli.py add --title "Bug title" --description "Detailed description" --priority high --assigned-to "Alice"
```

* `--priority` defaults to `low` if not specified.
* `--assigned-to` is optional.

#### Update an existing bug

```bash
python cli.py update <bug-id> --title "New title" --status "in_progress" --priority "medium" --assigned-to "Bob"
```

* Provide one or more fields to update.
* Bug IDs are UUID strings, e.g., `7f7ac788-3630-4f82-947d-9de3cd95f09f`.

#### Delete a bug

```bash
python cli.py delete <bug-id>
```

#### List all bugs (optional filters)

```bash
python cli.py list --status open --priority high
```

* Filters are optional. You can list all bugs with just `python cli.py list`.

#### Search bugs by keyword

```bash
python cli.py search "login failure"
```

* Searches in both title and description.

#### Add a comment to a bug

```bash
python cli.py comment <bug-id> "This bug needs urgent attention."
```

#### Update bug status

```bash
python cli.py status <bug-id> --to closed
```

* Valid statuses: `open`, `in_progress`, `resolved`, `closed`.

#### View bug details

```bash
python cli.py view <bug-id>
```

---

## 🐳 Using Docker

Build the Docker image:

```bash
docker build -t bug-reporter-cli .
```

Run commands inside the container (mount current directory as `/app`):

```bash
docker run --rm -v "$(pwd)":/app bug-reporter-cli add --title "Sample bug" --description "Details" --priority high
```

---

## 📜 Notes

* Bugs are stored in `bugs.json` in the project root.
* Bug IDs are UUID strings generated automatically.
* The CLI expects valid UUIDs for all operations involving bug IDs.
* Status updates and comments update the bug's `updated_at` timestamp.
* Feel free to extend with more features or integrate into your workflow.
