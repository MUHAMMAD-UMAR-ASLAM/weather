from utils import get_all_files_contents
from constants import  INDEX_LOOKUP

def get_unique_events_in_files():
    events = set()
    data = get_all_files_contents()
    for row in data:
        if row[INDEX_LOOKUP['unique_events']] != "":
            events.add(row[INDEX_LOOKUP['unique_events']])
    return events


get_unique_events_in_files()
