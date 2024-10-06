from status import status

class Entry:
    def __init__(self, parent: str, req_name: str, status: status.Status, ecd: str, assignee: str) -> None:
        self.parent = parent
        self.req_name = req_name
        self.status = status
        self.ecd = ecd
        self.assignee = assignee

    def __str__(self) -> str:
        res = f"{self.parent} - {self.req_name}"
        if self.status == status.Status.ONGOING:
            return f"{res} (ECD: {self.ecd})"
        else:
            return res