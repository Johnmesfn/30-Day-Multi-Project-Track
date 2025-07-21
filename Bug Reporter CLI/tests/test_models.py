import pytest
from bugs.models import Bug

def test_bug_creation():
    bug = Bug(
        title="Sample bug",
        description="Something is broken",
        priority="high",
        status="open",
        assigned_to="yohannes@example.com"
    )

    assert bug.title == "Sample bug"
    assert bug.description == "Something is broken"
    assert bug.priority == "high"
    assert bug.status == "open"
    assert bug.assigned_to == "yohannes@example.com"
    assert bug.id is not None
    assert bug.created_at is not None
    assert bug.updated_at is not None
