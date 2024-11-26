from utils import get_file_contents_by_year


def get_minimum_temperature(year):
    min = float('inf')
    data=get_file_contents_by_year(year)
    for row in data:
        if row[3] != "" and min > float(row[3]):
            min = float(row[3])
    return min


get_minimum_temperature(2011)
