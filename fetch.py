import csv
from datetime import datetime, timedelta

# csv file name
filename = "delay.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

required_date = str(input("Enter the date: "))
log = []
for i in range(0, len(rows)):
    if required_date == rows[i][0]:
        log.append(rows[i])

print(log)