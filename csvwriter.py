from os.path import exists
import csv


def csvwriter(headers, name, row):
    """Creates a cvs file if not exist, then write provided data"""
    if not exists(f'{name}.csv'):
        with open(f'{name}.csv', 'w', newline='') as file:
            csvfile = csv.writer(file)
            csvfile.writerow(headers)

    with open(f'{name}.csv', 'a+', newline='') as file:
        csvfile = csv.writer(file)
        csvfile.writerow(row)
