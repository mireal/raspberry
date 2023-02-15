import datetime

# import csv
# from os.path import exists
# import os
# for datafile in os.listdir('results'):
#
#     fields = ['Date', 'Time', 'Temperature', 'Humidity']
#
#     if not exists(f'{datafile}.csv'):
#         with open(f'{datafile}.csv', 'w', newline='') as file:
#             csvfile = csv.writer(file)
#             csvfile.writerow(fields)
#     with open(f'{datafile}.csv', 'a+', newline='') as file:
#
#         csvfile = csv.writer(file)
#         with open(f'results\{datafile}', 'r+') as textfile:
#             for line in textfile:
#                 line = line.split()
#                 line = line[0], line[1], line[3], line[6]
#                 csvfile.writerow(line)
#
#
#

last_record = datetime.datetime.now().strftime('%M')
print(last_record)