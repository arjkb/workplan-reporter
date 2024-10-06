from enum import Enum

class Group(Enum):
    DEV_COMPLETED = 'Dev Completed'
    ONGOING = 'Ongoing'
    UPCOMING = 'Upcoming'
    ON_HOLD = 'On Hold'

class Status(Enum):
    COMPLETED = 'Completed'
    DEV_COMPLETED = 'Dev Completed'
    WAITING_FOR_QA = 'Waiting for QA'
    ONGOING = 'Ongoing'
    PENDING = 'Pending'
    MOVED_TO_NEXT_SPRINT = 'Moved to next sprint'
    ON_HOLD = 'On Hold'
