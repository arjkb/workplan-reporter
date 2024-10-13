# Work Plan Reporter
# Arjun Krishna Babu

import csv
import datetime
import requests

from status import status
from workplan import entry, workplan

ASSIGNEE_NAME_POSSIBILITIES = ['Example Name', 'Example',]

# Generate WorkPlan from the csv file.
def generate_workplan_from_csv(csvfilename: str) -> workplan.WorkPlan:
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
                    if assignee in ASSIGNEE_NAME_POSSIBILITIES:
                        wp.add_entry(entry.Entry(curr_header, req_name, status.Status[stat.upper()], ecd, assignee))
    return wp

def main():
    # read URL from config
    with open('url.txt', 'r') as f:
        url = f.readline()
    print(url)

    # determine filenames
    DATE_FORMAT = '%Y%m%d'
    today = datetime.date.today()
    today_date_suffix = today.strftime(DATE_FORMAT)
    curr_week_fname = f"inputs/sprint_{today_date_suffix}.csv"
    prev_week_fname = f"inputs/sprint_{(today - datetime.timedelta(weeks=1)).strftime(DATE_FORMAT)}.csv"

    # fetch the file from the URL and save it to the appropriate location
    open(curr_week_fname, 'wb').write(requests.get(url).content)

    # make the workplan entry of that file
    curr_wp = generate_workplan_from_csv(curr_week_fname)
    print(curr_wp)

    # TODO: read last week's entry if available and subtract that from this week's entry

    # TODO: print the output

    # TODO: save the output to the clipboard

if __name__ == '__main__':
    main()
