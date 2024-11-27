from utils import get_all_files_contents
from constants import INDEX_LOOKUP

def get_dates_with_diff():
    dates = []
    data = get_all_files_contents()
    for row in data:
        if row[INDEX_LOOKUP['max_temperature']] != "" and row[INDEX_LOOKUP['min_temperature']] != "" and int(row[INDEX_LOOKUP['max_temperature']])-int(row[INDEX_LOOKUP['min_temperature']]) == 7:
            dates.append(row[0])
    return dates


get_dates_with_diff()
