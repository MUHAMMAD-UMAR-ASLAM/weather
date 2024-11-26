from utils import get_all_files_contents


def get_unique_events_in_files():
    events = set()
    data=get_all_files_contents()
    for row in data:
        if row[-2] != "":
            events.add(row[-2])
    return events


get_unique_events_in_files()
