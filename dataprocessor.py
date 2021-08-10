import csv
import sys

def presence_check(reading):
    return reading == None

def max_check(reading):
    return reading > 9.9

def min_check(reading):
    return reading < 0.0

def duplicate_batch(batch_ids):
    for batch_id in batch_ids:
        for batch_id2 in batch_ids:
            if batch_id == batch_id2:
                return True
    return False

file_name = input('Please enter your filename: ')
with open(file_name, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    batch_ids = []
    for row in csv_reader:
        for field in row:
            if (presence_check(row[field])):
                print(f"File invalid. The data for batch_id {row['batch_id']} is missing at least one reading")
                sys.exit()
        readings = [float(row['reading1']), float(row['reading2']), float(row['reading3']), float(row['reading4']),
                    float(row['reading5']), float(row['reading6']), float(row['reading7']), float(row['reading8']),
                    float(row['reading9']), float(row['reading10'])]
        for reading in readings:
            print(reading)
            if max_check(reading):
                print("File invalid. Reading value {reading} for batch id {row['batch_id']} exceeds max value 9.9")
                sys.exit()
            elif min_check(reading):
                print("File invalid. Reading value {reading} for batch id {row['batch_id']} below min value 0.0")
                sys.exit()
        batch_ids.append(int(row['batch_id']))
    if duplicate_batch(batch_ids):
        print("File invalid. There are duplicate batch ids in the file")
        sys.exit()
    print("File valid. Storing...")


