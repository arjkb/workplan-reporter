class Entry:
    def __init__(self, parent: str, req_name: str, status: str, ecd: str, assignee: str) -> None:
        self.parent = parent
        self.req_name = req_name
        self.status = status
        self.ecd = ecd
        self.assignee = assignee

    def __str__(self) -> str:
        res = f"{self.parent} - {self.req_name}"
        if self.status == 'Ongoing':
            return f"{res} (ECD: {self.ecd})"
        else:
            return res