from os.path import exists
import csv


def csvwriter(headers, filename, rows):
    """Creates a cvs file if not exist, then write provided data"""
    if not exists(f'{filename}.csv'):
        with open(f'{filename}.csv', 'w', newline='') as file:
            csvfile = csv.writer(file)
            csvfile.writerow(headers)

    with open(f'{filename}.csv', 'a+', newline='') as file:
        csvfile = csv.writer(file)
        csvfile.writerow(rows)
