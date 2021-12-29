import enum


class RoleType(enum.Enum):
    student = "student"
    coach = "coach"
    admin = "admin"


class State(enum.Enum):
    pending = "pending"
    added = "added"
    rejected = "rejected"
