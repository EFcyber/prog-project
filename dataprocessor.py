import csv

#checks that all fields in the file have been filled
def presence_check(reading):
    return reading == None

#checks that no reading value exceeds 9.9
def max_check(reading):
    return reading > 9.9

#checks that no reading value is below 0.0
def min_check(reading):
    return reading < 0.0

#checks that there are no duplicate batch ids in the file
def duplicate_batch(batch_ids):
    for i in range(len(batch_ids)):
        for j in range(i+1, len(batch_ids)):
            if batch_ids[i] == batch_ids[j]:
                return True
    return False

#reads in the file and performs data verification
def verifier(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #used to store the values of the batch ids in the file for duplicate checking
        batch_ids = []
        #iterates through each row in the file
        for row in csv_reader:
            for field in row:
                #returns FAILURE if there are fields with no data in them
                if (presence_check(row[field])):
                    print(f"File invalid. The data for batch_id {row['batch_id']} is missing at least one reading")
                    return "FAILURE"
            #used to store the values of all readings so they may be individually verified
            readings = [float(row['reading1']), float(row['reading2']), float(row['reading3']), float(row['reading4']),
                        float(row['reading5']), float(row['reading6']), float(row['reading7']), float(row['reading8']),
                        float(row['reading9']), float(row['reading10'])]
            #iterates through each reading in the row
            for reading in readings:
                #returns FAILURE if the current reading exceeds 9.9
                if max_check(reading):
                    print(f"File invalid. Reading value {reading} for batch id {row['batch_id']} exceeds max value 9.9")
                    return "FAILURE"
                #returns FAILURE if the current reading is below 0.0
                elif min_check(reading):
                    print(f"File invalid. Reading value {reading} for batch id {row['batch_id']} below min value 0.0")
                    return "FAILURE"
            #adds the batch id of the current row to the list
            batch_ids.append(int(row['batch_id']))
        #returns FAILURE if the same batch id appears more than once in the file
        if duplicate_batch(batch_ids):
            print("File invalid. There are duplicate batch ids in the file")
            return "FAILURE"
        #returns SUCCESS if the file has passed all above verification checks
        return "SUCCESS"

def main():
    #for testing purposes, the CSV filename is input by the user in the terminal
    file_name = input("Please enter a filename: ")
    #result of the verification is printed, either SUCCESS or FAILURE
    print(verifier(file_name))

if __name__ == "__main__":
    main()

