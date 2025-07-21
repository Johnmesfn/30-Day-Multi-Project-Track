import os
import tempfile
import json
from bugs import manager

def setup_function():
    # Use a temporary file as a fake bugs.json
    manager.Bug_FILE = tempfile.NamedTemporaryFile(delete=False).name

def teardown_function():
    if os.path.exists(manager.Bug_FILE):
        os.remove(manager.Bug_FILE)

def test_add_bug():
    bug = manager.add_bug("Test Bug", "This is a test", "medium", assigned_to="dev1")
    assert bug.title == "Test Bug"
    assert bug.priority == "medium"
    assert bug.status == "open"

def test_update_bug():
    bug = manager.add_bug("Old Title", "Old Desc", "low")
    updated = manager.update_bug(str(bug.id), title="New Title", status="closed")
    assert updated.title == "New Title"
    assert updated.status == "closed"

def test_delete_bug():
    bug = manager.add_bug("To Delete", "Bye", "high")
    deleted = manager.delete_bug(str(bug.id))
    assert deleted is True
    # Should not find the bug again
    bugs = manager.load_bugs()
    assert all(str(b.id) != str(bug.id) for b in bugs)
