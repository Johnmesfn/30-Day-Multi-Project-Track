import json
import os
from datetime import datetime
from .models import Bug

BUG_FILE = 'bugs.json'

def load_bugs(filename=BUG_FILE):
    """Load bugs from the JSON file."""
    if not os.path.exists(filename):
        print(f"{filename} not found. No bugs loaded.")
        return []
    try:
        with open(filename, 'r') as file:
            bugs_data = json.load(file)
            if not bugs_data:
                print(f"{filename} is empty.")
            return [Bug.from_dict(bug) for bug in bugs_data]
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error loading bugs: {e}")
        return []

def save_bugs(bugs, filename=BUG_FILE):
    """Save bugs to the JSON file."""
    for bug in bugs:
        # Ensure all attributes are present in the bug object
        if not hasattr(bug, 'id') or not hasattr(bug, 'created_at') or not hasattr(bug, 'updated_at'):
            raise ValueError("Bug is missing required attributes.")
    with open(filename, 'w') as file:
        json.dump([bug.to_dict() for bug in bugs], file, indent=4)

def add_bug(title, description, priority, status='open', assigned_to=None, tags=None, filename=BUG_FILE):
    """Add a new bug."""
    bugs = load_bugs(filename)
    new_bug = Bug(title, description, priority, assigned_to=assigned_to, tags=tags)
    bugs.append(new_bug)
    save_bugs(bugs, filename)
    return new_bug

def update_bug(bug_id, title=None, description=None, priority=None, status=None, assigned_to=None, filename=BUG_FILE):
    """Update an existing bug."""
    bugs = load_bugs(filename)
    for bug in bugs:
        if str(bug.id) == bug_id:
            if title is not None:
                bug.title = title
            if description is not None:
                bug.description = description
            if priority is not None:
                bug.priority = priority
            if status is not None:
                bug.status = status
            if assigned_to is not None:
                bug.assigned_to = assigned_to
            bug.updated_at = datetime.now()
            save_bugs(bugs, filename)
            return bug
    raise ValueError(f"Bug with ID {bug_id} not found.")

def delete_bug(bug_id, filename=BUG_FILE):
    """Delete a bug by its ID."""
    bugs = load_bugs(filename)
    for i, bug in enumerate(bugs):
        if str(bug.id) == bug_id:
            del bugs[i]
            save_bugs(bugs, filename)
            return True
    raise ValueError(f"Bug with ID {bug_id} not found (could not be deleted).")

def list_bugs(status=None, priority=None, filename=BUG_FILE):
    """List all bugs, optionally filtered by status and priority."""
    bugs = load_bugs(filename)
    filtered_bugs = []
    for bug in bugs:
        if status and bug.status != status:
            continue
        if priority and bug.priority != priority:
            continue
        filtered_bugs.append(bug)
    return filtered_bugs

def search_bugs(query, filename=BUG_FILE):
    """Search bugs by title or description."""
    bugs = load_bugs(filename)
    query = query.lower()
    return [bug for bug in bugs if query in bug.title.lower() or query in bug.description.lower()]

def add_comment(bug_id, comment, filename=BUG_FILE):
    """Add a comment to a bug."""
    bugs = load_bugs(filename)
    for bug in bugs:
        if str(bug.id) == bug_id:
            timestamp = datetime.now().isoformat()
            bug.comments.append(f"[{timestamp}] {comment}")
            bug.updated_at = datetime.now()
            save_bugs(bugs, filename)
            return bug
    raise ValueError(f"Bug with ID {bug_id} not found for commenting.")

def get_bug_by_id(bug_id, filename=BUG_FILE):
    """Retrieve a bug by its ID."""
    bugs = load_bugs(filename)
    for bug in bugs:
        if str(bug.id) == bug_id:
            return bug
    raise ValueError(f"Bug with ID {bug_id} not found.")

def update_status(bug_id, new_status, filename=BUG_FILE):
    """Update the status of a bug."""
    if new_status not in Bug.VALID_STATUSES:
        raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {', '.join(Bug.VALID_STATUSES)}")
    bugs = load_bugs(filename)
    for bug in bugs:
        if str(bug.id) == bug_id:
            bug.status = new_status
            bug.updated_at = datetime.now()
            save_bugs(bugs, filename)
            return bug
    raise ValueError(f"Bug with ID {bug_id} not found.")
