# importing csv module
import csv
from datetime import datetime, timedelta, date

# csv file name
filename = "churchgate_up.csv"

# initializing the titles and rows list
fields_up = []
rows_up = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields_up = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows_up.append(row)

# csv file name
filename = "virar_down.csv"

# initializing the titles and rows list
fields_down = []
rows_down = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields_down = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows_down.append(row)

# fetching current time
x = datetime.now()
x = x.strftime("%H") + ":" + x.strftime("%M")

# converting x into a time variable again
x = x.split(":")
x = timedelta(hours=int(x[0]), minutes=int(x[1]))

a = str(input("Enter source station: "))
b = str(input("Enter destination station: "))

if fields_up.index(b) > fields_up.index(a):
    a_i = fields_up.index(a)
    b_i = fields_up.index(b)
    rows = rows_up
    fields = fields_up

else:
    a_i = fields_down.index(a)
    b_i = fields_down.index(b)
    rows = rows_down
    fields = fields_down

trains = []
for i in range(0, len(rows_up)):
    details = []
    if rows[i][a_i]:
        if rows[i][b_i]:
            details.append(rows[i][0])
            details.append(rows[i][a_i])
            details.append(rows[i][b_i])
            t = rows[i][a_i]
            t = t.split(":")
            t = timedelta(hours=int(t[0]), minutes=int(t[1]))
            if x <= t:
                details.append(True)
            else:
                details.append(False)

            trains.append(details)

print(trains)