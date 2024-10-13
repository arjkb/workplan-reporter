# Work Plan Reporter
# Arjun Krishna Babu

import datetime
import requests


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

    # fetch the file from the URL and save it to the appropriate directory
    open(curr_week_fname, 'wb').write(requests.get(url).content)

    # TODO: make the workplan entry of that file

    # TODO: read last week's entry if available and subtract that from this week's entry

    # TODO: print the output

    # TODO: save the output to the clipboard

if __name__ == '__main__':
    main()
