import json
import os
from datetime import datetime
from bugs.models import Bug

BUG_FILE = 'bugs.json'

def load_bugs():
    if not os.path.exists(BUG_FILE):
        return []
    try:
        with open(BUG_FILE, 'r') as file:
            bugs_data = json.load(file)
            return [Bug(**bug) for bug in bugs_data]
    except json.JSONDecodeError:
        print("Error: Invalid JSON data in bugs.json")
        return []
    except Exception as e:
        print(f"Error loading bugs: {e}")
        return []
    
def print_bugs():
    bugs = load_bugs()
    if not bugs:
        print("No bugs found.")
    else:
        print("\nAvailable Bugs:")
        for bug in bugs:
            print(f"  [{bug.id}] {bug.title} - Priority: {bug.priority}, Status: {bug.status}")
        
def save_bugs(bugs):
    with open(BUG_FILE, 'w') as file:
        json.dump([bug.to_dict() for bug in bugs], file, indent=4)

def add_bug(title, description, priority, assigned_to=None):
    bugs = load_bugs()
    new_bug = Bug(title, description, priority, assigned_to=assigned_to)
    bugs.append(new_bug)
    save_bugs(bugs)
    return new_bug

def update_bug(bug_id, title=None, description=None, priority=None, status=None, assigned_to=None):
    bugs = load_bugs()
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
            save_bugs(bugs)
            return bug
    return None

def delete_bug(bug_id):
    bugs = load_bugs()
    for i, bug in enumerate(bugs):
        if str(bug.id) == bug_id:
            del bugs[i]
            save_bugs(bugs)
            return True
    return False