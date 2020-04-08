# importing csv module
import csv
import datetime

# csv file name 
filename = "churchgate_up.csv"

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


# fetching current time
x = datetime.datetime.now()
x = x.strftime("%H") + ":" + x.strftime("%M")

# checking running trains
transit = []

for i in range(0, len(rows)):
    schedule = []
    details = []
    stations = []
    for j in range(3, len(rows[i])):
        if rows[i][j]:
            schedule.append(rows[i][j])
            stations.append(fields[j])

    if schedule[0] < x < schedule[-1]:
        details.append(rows[i][0])
        flag = True

        # for trains in stations
        for k in range(0, len(schedule)):
            if schedule[k] == x:
                s = True
                details.append(stations[k])
                details.append(s)
                flag = False
                break

        # for trains not in stations
        if flag:
            for k in range(0, len(schedule)):
                if schedule[k] > x:
                    s = False
                    details.append(stations[k - 1])
                    details.append(s)
                    flag = False
                    break

        transit.append(details)

# current status data
print(transit)
