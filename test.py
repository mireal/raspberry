import csv
import pickle
import os

path = '.\\results\\'
csv_files = [f for f in os.listdir(path)]
pickle_file = 'data.pickle'
filtered_file = 'filtered_data.pickle'

def csv_to_pickle(csv_files, pickle_file):
    all_rows = []
    for csv_file in csv_files:
        with open(os.path.join(path, csv_file), 'r') as csv_f:
            reader = csv.reader(csv_f)
            headers = next(reader) # ignore header of csv files
            for row in reader:
                all_rows.append(row)

    with open(pickle_file, 'wb') as f:
        pickle.dump(all_rows, f)

def filter_by_minute(input_file, output_file):
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        headers = pickle.load(f_in)
        pickle.dump(headers, f_out)
        last_minute = None
        for row in pickle.load(f_in):
            time_parts = row[1].split(':')
            minute = time_parts[1]
            if last_minute != minute:
                pickle.dump(row, f_out)
                last_minute = minute


# filter_by_minute('data.pickle','filtered_data.pickle')
# csv_to_pickle(csv_files, pickle_file)

with open(filtered_file, 'rb') as file:
    my_data = pickle.load(file)
    for row in my_data:
        print(row)