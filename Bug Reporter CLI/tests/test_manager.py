import tempfile
import os
import pytest
from bugs import manager

@pytest.fixture
def temp_bug_file():
    # Create a temporary file and set it as the bug file for manager
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        manager.BUG_FILE = tmp.name
        yield tmp.name
    # Cleanup after test
    if os.path.exists(tmp.name):
        os.remove(tmp.name)

def test_add_bug(temp_bug_file):
    bug = manager.add_bug("Test Bug", "Testing add bug", "medium")
    assert bug.title == "Test Bug"
    assert bug.priority == "medium"
    assert bug.status == "open"
    assert os.path.exists(temp_bug_file)

def test_update_bug(temp_bug_file):
    bug = manager.add_bug("Old Bug", "Old desc", "low")
    updated = manager.update_bug(str(bug.id), title="Updated Bug", status="closed")
    assert updated.title == "Updated Bug"
    assert updated.status == "closed"

def test_delete_bug(temp_bug_file):
    bug = manager.add_bug("Delete Me", "Delete this bug", "high")
    result = manager.delete_bug(str(bug.id))
    assert result is True
    bugs = manager.load_bugs()
    assert all(str(b.id) != str(bug.id) for b in bugs)

def test_list_bugs(temp_bug_file):
    manager.add_bug("Bug One", "Desc one", "low", status="open")
    manager.add_bug("Bug Two", "Desc two", "high", status="closed")
    all_bugs = manager.list_bugs()
    open_bugs = manager.list_bugs(status="open")
    assert len(all_bugs) >= 2
    assert all(b.status == "open" for b in open_bugs)

def test_update_status(temp_bug_file):
    bug = manager.add_bug("Status Bug", "Status test", "medium")
    updated = manager.update_status(str(bug.id), "resolved")
    assert updated.status == "resolved"
