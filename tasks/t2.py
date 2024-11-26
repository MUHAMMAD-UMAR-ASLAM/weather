from utils import get_file_contents_by_year


def get_minimum_temperature(year):
    max_value = float('-inf')
    data=get_file_contents_by_year(year)
    for row in data:
        if row[1] != "" and max_value < float(row[1]):
            max_value = float(row[1])
    return max_value


get_minimum_temperature(2011)
