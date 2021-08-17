---
layout: default
title: dataprocessor.py
parent: Function Documentation
---
# dataprocessor.py
This script is responsible for processing CSV files containing medical data.
The data has specific constraints, including no duplicate batch ids, no missing data in any fields, and readings must have a value in between 0.0 and 9.9.

## presence_check
This function is used to check that a field has been filled by returning whether or not the function input is equal to None.
```python
presence_check(reading)
```

### Example use of presence_check
```python
if (presence_check(row[field])):
    print(f"File invalid. The data for batch_id {row['batch_id']} is missing at least one reading")
    return "FAILURE"
```
This code appears in the [verifier](#verifier) function in a loop which iterates through all fields in the parsed CSV file and returns "FALSE" if a field is equal to None.

## max_check
This function is used to check if a field has a greater value than 9.9. 
```python
max_check(reading)
```

### Example use of max_check
```python
if max_check(reading):
    print(f"File invalid. Reading value {reading} for batch id {row['batch_id']} exceeds max value 9.9")
    return "FAILURE"
```
This code appears in the [verifier](#verifier) function in a loop which iterates through an array containing all readings in a row in a CSV file. 
It returns "FALSE" if any reading is greater than 9.9.

## min_check
This function is used to check if a field has a lower value than 0.0. 
```python
min_check(reading)
```

### Example use of min_check
```python
if min_check(reading):
    print(f"File invalid. Reading value {reading} for batch id {row['batch_id']} below min value 0.0")
    return "FAILURE"
```
This code appears in the [verifier](#verifier) function in a loop which iterates through an array containing all readings in a row in a CSV file. 
It returns "FALSE" if any reading is lower than 0.0.


## duplicate_batch
This function is used to check that there are no duplicate batch ids in the input CSV file.
```python
duplicate_batch(batch_ids)
```

### Example use of duplicate_batch
```python
if duplicate_batch(batch_ids):
    print("File invalid. There are duplicate batch ids in the file")
    return "FAILURE"
```
This code appears in the [verifier](#verifier) function. During the function's search through the file, it adds the batch id of each row to a list.
When the loop has completed, the function is called on this list to see if any two elements of the list share the same value.
The verifier function returns "FALSE" if this is the case.

## verifier<a name="verifier"></a>
This function is used to verify that a CSV file meets all constraints detailed in the function descriptions above. 
If it passes all constraints, it returns "SUCCESS". If any of them are breached, it returns "FAILURE".
```python
verifier(file_name)
```

### Example use of presence_check
```python
file_name = input("Please enter a filename: ")
    #result of the verification is printed, either SUCCESS or FAILURE
    print(verifier(file_name))
```
This code makes up the entirety of the main function. 
To allow the script to run on its own for testing purposes, the filename of the CSV to be verified is input in the terminal.
This input filename is stored in a variable which is then passed to the verifier function.
The script prints the result "SUCCESS" or "FAILURE" depending on what the function returns as a result of calling the functions described above.