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

    def __sub__(self, other):
        result = WorkPlan()

        # entries of these groups from last week must be excluded from this week
        groups_to_exclude_from_other = ['Dev Completed', 'On Hold']
        exclusions = []
        for group in groups_to_exclude_from_other:
            exclusions.extend([e.req_name for e in other.grouped_entries[group]])

        for group in self.grouped_entries:
            for wpe in self.grouped_entries[group]:
                if wpe.req_name in exclusions and group in groups_to_exclude_from_other:
                    continue
                result.add_entry(wpe)

        # ongoing from last week must be part of dev-completed of the difference
        # if it is still not ongoing this week
        dev_completed_curr = [e.req_name for e in self.grouped_entries['Dev Completed']]
        ongoing_curr = [e.req_name for e in self.grouped_entries['Ongoing']]
        for wpe_ongoing_prev in other.grouped_entries['Ongoing']:
            if wpe_ongoing_prev.req_name not in dev_completed_curr and wpe_ongoing_prev.req_name not in ongoing_curr:
                result.add_entry_as_completed(wpe_ongoing_prev)

        return result

    def add_entries(self, wpes) -> None:
        for wpe in wpes:
            self.add_entry(wpe)

    def add_entry(self, wpe) -> None:
        for group in self.status_mappings:
            for status in self.status_mappings[group]:
                if status == wpe.status:
                    self.grouped_entries[group].append(wpe)
                    break

    def add_entry_as_completed(self, wpe) -> None:
        wpe.status = 'Dev Completed'
        self.add_entry(wpe)

    def __str__(self) -> str:
        result = ""
        for group in self.grouped_entries:
            if len(self.grouped_entries[group]) > 0:
                result += f"\n\n{group}\n"
                result += "\n".join(
                    [str(item) for item in self.grouped_entries[group]]
                )
        return result
