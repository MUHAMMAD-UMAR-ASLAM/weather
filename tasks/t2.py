from utils import get_file_contents_by_year
from constants import  INDEX_LOOKUP

def get_maximum_temperature(year):
    max_value = float('-inf')
    data = get_file_contents_by_year(year)
    for row in data:
        if row[INDEX_LOOKUP['max_temperature']] != "" and max_value < float(row[INDEX_LOOKUP['max_temperature']]):
            max_value = float(row[1])
    return max_value


get_maximum_temperature(2011)
