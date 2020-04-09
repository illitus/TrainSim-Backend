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

filename_d = "distance_up.csv"

# initializing the titles and rows list
fields_d_up = []
rows_d_up = []

# reading csv file
with open(filename_d, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields_d_up = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows_d_up.append(row)


filename_d_down = "distance_down.csv"

# initializing the titles and rows list
fields_d_down = []
rows_d_down = []

# reading csv file
with open(filename_d_down, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields_d_down = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows_d_down.append(row)

# fetching current time
x = datetime.now()
x = x.strftime("%H") + ":" + x.strftime("%M")

# converting x into a time variable again
x = x.split(":")
x = timedelta(hours=int(x[0]), minutes=int(x[1]))

b = str(input("Enter station: "))

# for up line
if fields_up.index(b):
    b_i = fields_up.index(b)

trains = []
for i in range(0, len(rows_up)):
    details = []
    flag = False
    flag1 = True
    if rows_up[i][b_i]:
        b_t = rows_up[i][b_i]
        b_t = b_t.split(":")
        b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
        if b_t <= x:
            for j in range(b_i+1, len(rows_up[i])):
                if flag1:
                    if rows_up[i][j]:
                        c_i = j
                        c_t = rows_up[i][j]
                        c = fields_up[j]
                        c_t = c_t.split(":")
                        c_t = timedelta(hours=int(c_t[0]), minutes=int(c_t[1]))
                        if b_t <= x <= c_t:
                            flag = True
                            flag1 = False
                        break


            if flag:
                for p in range(0, len(rows_d_up)):
                    if b == rows_d_up[p][0]:
                        d_b = float(rows_d_up[p][1])
                    if c == rows_d_up[p][0]:
                        d_c = float(rows_d_up[p][1])

                t_dist = d_c - d_b

                # calculting total time
                time = c_t - b_t
                time = str(time)
                time = time.split(":")
                # calculating current time
                time_c = x - b_t
                time_c = str(time_c)
                time_c = time_c.split(":")
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                details.append(rows_up[i][0])
                details.append(b)
                details.append(round(i_dist,2 ))
                details.append(c)
                # print(i_dist)
                trains.append(details)

for i in range(0, len(rows_up)):
    details = []
    flag = False
    flag1 = True
    if rows_up[i][b_i]:
        b_t = rows_up[i][b_i]
        b_t = b_t.split(":")
        b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
        if b_t >= x:
            for j in range(b_i-1, 2, -1):
                if flag1:
                    if rows_up[i][j]:
                        a_i = j
                        a_t = rows_up[i][j]
                        a = fields_up[j]
                        a_t = a_t.split(":")
                        a_t = timedelta(hours=int(a_t[0]), minutes=int(a_t[1]))
                        if a_t <= x <= b_t:
                            flag = True
                            flag1 = False
                        break


            if flag:
                for p in range(0, len(rows_d_up)):
                    if b == rows_d_up[p][0]:
                        d_b = float(rows_d_up[p][1])
                    if a == rows_d_up[p][0]:
                        d_a = float(rows_d_up[p][1])

                t_dist = d_b - d_a

                # calculting total time
                time = b_t - a_t
                time = str(time)
                time = time.split(":")
                # calculating current time
                time_c = x - a_t
                time_c = str(time_c)
                time_c = time_c.split(":")
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                details.append(rows_up[i][0])
                details.append(a)
                details.append(round(i_dist, 2))
                details.append(b)
                # print(i_dist)
                trains.append(details)

# virar down line

if fields_down.index(b):
    b_i = fields_down.index(b)

for i in range(0, len(rows_down)):
    details = []
    flag = False
    flag1 = True
    if rows_down[i][b_i]:
        b_t = rows_down[i][b_i]
        b_t = b_t.split(":")
        b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
        if b_t <= x:
            for j in range(b_i+1, len(rows_down[i])):
                if flag1:
                    if rows_down[i][j]:
                        c_i = j
                        c_t = rows_down[i][j]
                        c = fields_down[j]
                        c_t = c_t.split(":")
                        c_t = timedelta(hours=int(c_t[0]), minutes=int(c_t[1]))
                        if b_t <= x <= c_t:
                            flag = True
                            flag1 = False
                        break


            if flag:
                for p in range(0, len(rows_d_down)):
                    if b == rows_d_down[p][0]:
                        d_b = float(rows_d_down[p][1])
                    if c == rows_d_down[p][0]:
                        d_c = float(rows_d_down[p][1])

                t_dist = d_c - d_b

                # calculting total time
                time = c_t - b_t
                time = str(time)
                time = time.split(":")
                # calculating current time
                time_c = x - b_t
                time_c = str(time_c)
                time_c = time_c.split(":")
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                details.append(rows_down[i][0])
                details.append(b)
                details.append(round(i_dist, 2))
                details.append(c)
                # print(i_dist)
                trains.append(details)

for i in range(0, len(rows_down)):
    details = []
    flag = False
    flag1 = True
    if rows_down[i][b_i]:
        b_t = rows_down[i][b_i]
        b_t = b_t.split(":")
        b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
        if b_t >= x:
            for j in range(b_i-1, 2, -1):
                if flag1:
                    if rows_down[i][j]:
                        a_i = j
                        a_t = rows_down[i][j]
                        a = fields_down[j]
                        a_t = a_t.split(":")
                        a_t = timedelta(hours=int(a_t[0]), minutes=int(a_t[1]))
                        if a_t <= x <= b_t:
                            flag = True
                            flag1 = False
                        break


            if flag:
                for p in range(0, len(rows_d_down)):
                    if b == rows_d_down[p][0]:
                        d_b = float(rows_d_down[p][1])
                    if a == rows_d_down[p][0]:
                        d_a = float(rows_d_down[p][1])

                t_dist = d_b - d_a

                # calculting total time
                time = b_t - a_t
                time = str(time)
                time = time.split(":")
                # calculating current time
                time_c = x - a_t
                time_c = str(time_c)
                time_c = time_c.split(":")
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                details.append(rows_down[i][0])
                details.append(a)
                details.append(round(i_dist, 2))
                details.append(b)
                # print(i_dist)
                trains.append(details)

print(trains)