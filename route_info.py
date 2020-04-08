import csv
from datetime import datetime, timedelta, date

route = str(input("Enter Route Code: "))

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

route_info = []
details = []
flag = True

for i in range(0, len(rows_up)):
    if route == rows_up[i][0]:
        route_info.append(fields_up[3:])
        for k in range(3, len(rows_up[i])):
            if rows_up[i][k]:
                details.append(rows_up[i][k])
            else:
                details.append('-')
        route_info.append(details)
        flag = False
        break

if flag:
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

        for i in range(0, len(rows_down)):
            if route == rows_down[i][0]:
                route_info.append(fields_down[3:])
                for k in range(3, len(rows_down[i])):
                    if rows_down[i][k]:
                        details.append(rows_down[i][k])
                    else:
                        details.append('-')
                route_info.append(details)
                flag = False
                break

print(route_info)