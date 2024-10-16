# Work Plan Reporter
# Arjun Krishna Babu

import csv
import datetime
import os
import requests
import subprocess
import sys

from status import status
from workplan import entry, workplan

# Generate WorkPlan from the csv file.
def generate_workplan_from_csv(csvfilename: str, assignees: list[str]) -> workplan.WorkPlan:
    curr_header = ''
    wp = workplan.WorkPlan()
    with open(csvfilename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if any(map(lambda cols: len(cols) > 0, row)): # only go through rows with content
                if len(row[0]) > 0 and all(map(lambda col: len(col) == 0, row[1:])):
                    # if the row only had content in the first column, then it is a header row
                    curr_header = row[0]
                else:
                    req_name, stat, ecd, assignee = row[0], row[4], row[9], row[10]
                    if assignee in assignees:
                        wp.add_entry(entry.Entry(curr_header, req_name, status.Status[stat.upper()], ecd, assignee))
    return wp

def main():
    DATE_FORMAT = '%Y%m%d'
    today = datetime.date.today()
    today_date_suffix = today.strftime(DATE_FORMAT)
    date_string = today.strftime("%a %-d %b %Y")
    curr_week_fname = f"inputs/sprint_{today_date_suffix}.csv"
    prev_week_fname = f"inputs/sprint_{(today - datetime.timedelta(weeks=1)).strftime(DATE_FORMAT)}.csv"
    output_fname = f"outputs/sprint_report_{today_date_suffix}.csv"

    with open('config.txt', 'r') as f:
        lines = f.readlines()
        url = lines[0].strip()
        assignee_names = [assignee_name.strip() for assignee_name in lines[1].strip().split(',')]

    # fetch the file from the URL and save it to the appropriate location
    open(curr_week_fname, 'wb').write(requests.get(url).content)

    # make the workplan entries of current and previous weeks
    curr_wp = generate_workplan_from_csv(curr_week_fname, assignee_names) if os.path.isfile(curr_week_fname) else None
    if curr_wp is None:
        print("failed to generate current week's file")
        sys.exit(-1)

    if os.path.isfile(prev_week_fname):
        result_wp = curr_wp - generate_workplan_from_csv(prev_week_fname, assignee_names)
    else:
        result_wp = curr_wp

    output_text = (
        f"Weekly report for the week ending on {date_string}."
        + str(result_wp)
        + "\n\nIn the unlikely event of a mismatch between Jira and the workplan, prefer entry in the latter."
    )

    print(output_text)

    open(output_fname, 'w').write(output_text)

    # copy to clipboard
    subprocess.run('pbcopy', text=True, input=output_text)

if __name__ == '__main__':
    main()
