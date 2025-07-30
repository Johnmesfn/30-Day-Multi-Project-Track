import os
import tempfile
import json
from bugs import manager

def setup_function(function):
    # Create a temporary bug file for each test
    global test_file
    temp = tempfile.NamedTemporaryFile(delete=False)
    test_file = temp.name
    temp.close()

def teardown_function(function):
    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_bug():
    bug = manager.add_bug("Test Bug", "This is a test", "medium", assigned_to="dev1", filename=test_file)
    assert bug.title == "Test Bug"
    assert bug.priority == "medium"
    assert bug.status == "open"

def test_update_bug():
    bug = manager.add_bug("Old Title", "Old Desc", "low", filename=test_file)
    updated = manager.update_bug(str(bug.id), title="New Title", status="closed", filename=test_file)
    assert updated.title == "New Title"
    assert updated.status == "closed"

def test_delete_bug():
    bug = manager.add_bug("To Delete", "Bye", "high", filename=test_file)
    deleted = manager.delete_bug(str(bug.id), filename=test_file)
    assert deleted is True
    bugs = manager.load_bugs(filename=test_file)
    assert all(str(b.id) != str(bug.id) for b in bugs)

def test_update_status():
    bug = manager.add_bug("Sample Bug", "Something is broken", "medium", assigned_to="Alice", filename=test_file)
    manager.update_status(str(bug.id), "resolved", filename=test_file)
    bugs = manager.load_bugs(filename=test_file)
    updated_bug = next(b for b in bugs if str(b.id) == str(bug.id))
    assert updated_bug.status == "resolved"
