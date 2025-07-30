import uuid
from datetime import datetime

class Bug:
    VALID_STATUSES = ["open", "in_progress", "resolved", "closed"]
    def __init__(self, title, description, priority, status='open', assigned_to=None,
                 id=None, created_at=None, updated_at=None, comments=None):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}. Valid statuses are: {', '.join(self.VALID_STATUSES)}")
        self.id = uuid.UUID(id) if id else uuid.uuid4()
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to
        self.created_at = datetime.fromisoformat(created_at) if created_at else datetime.now()
        self.updated_at = datetime.fromisoformat(updated_at) if updated_at else self.created_at
        self.comments = comments if comments else []

    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "assigned_to": self.assigned_to,
            "comments": self.comments
        }
