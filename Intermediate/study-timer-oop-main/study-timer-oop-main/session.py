from dataclasses import dataclass


@dataclass
class Session:
    """Current session data and user statistics."""

    objective: str = ""
    notes: str = ""
    completed: int = 0

    @property
    def current_number(self):
        return self.completed % 4 + 1

    def complete(self):
        self.completed += 1

