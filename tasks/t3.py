from utils import get_all_files_contents


def get_dates_with_diff():
    dates = []
    data = get_all_files_contents()
    for row in data:
        if row[1] != "" and row[3] != "" and int(row[1])-int(row[3]) == 7:
            dates.append(row[0])
    return dates


get_dates_with_diff()
