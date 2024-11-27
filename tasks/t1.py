from utils import get_file_contents_by_year
from constants import  INDEX_LOOKUP


def get_minimum_temperature(year):
    min = float('inf')
    data = get_file_contents_by_year(year)
    for row in data:
        if row[INDEX_LOOKUP['min_temperature']] != "" and min > float(row[INDEX_LOOKUP['min_temperature']]):
            min = float(row[INDEX_LOOKUP['min_temperature']])
    return min


get_minimum_temperature(2011)
