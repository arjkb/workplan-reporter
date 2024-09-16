class WorkPlan:
    # mappings from report status to sheet status
    status_mappings = {
        'Dev Completed': ['Completed', 'Dev Completed', 'Waiting for QA'],
        'Ongoing': ['Ongoing'],
        'Upcoming': ['Pending', 'Moved to next sprint'],
        'On Hold': ['On Hold'],
    }

    def __init__(self):
        self.grouped_entries = {}
        for group in self.status_mappings:
            self.grouped_entries[group] = []

    def add_entries(self, wpes) -> None:
        for wpe in wpes:
            self.add_entry(wpe)

    def add_entry(self, wpe) -> None:
        for group in self.status_mappings:
            for status in self.status_mappings[group]:
                if status == wpe.status:
                    self.grouped_entries[group].append(wpe)
                    break

    def __str__(self) -> str:
        result = ""
        for group in self.grouped_entries:
            if len(self.grouped_entries[group]) > 0:
                result += f"\n\n{group}\n"
                result += "\n".join(
                    [str(item) for item in self.grouped_entries[group]]
                )
        return result
