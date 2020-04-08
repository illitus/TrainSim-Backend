# importing csv module
import csv
from datetime import datetime, timedelta, date

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
x = datetime.now()
x = x.strftime("%H") + ":" + x.strftime("%M")

# converting x into a time variable again
x = x.split(":")
x = timedelta(hours=int(x[0]), minutes=int(x[1]))

# checking running trains
transit = []

for i in range(0, len(rows)):
    schedule = []
    details = []
    stations = []
    for j in range(3, len(rows[i])):
        if rows[i][j]:
            # schedule.append(rows[i][j])
            t = rows[i][j]
            t = t.split(":")
            t = timedelta(hours=int(t[0]), minutes=int(t[1]))
            schedule.append(t)
            stations.append(fields[j])

    # print(schedule)

    if schedule[0] < x < schedule[-1]:
        transit.append(rows[i][0])


# current status data
print(transit)

route = str(input("Enter Route Code: "))

schedule = []
stations = []

for i in range(0, len(rows)):
    if route == rows[i][0]:
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])

print(stations)
# distance data


# csv file name
filename_d = "distance_up.csv"

# initializing the titles and rows list
fields_d = []
rows_d = []

# reading csv file
with open(filename_d, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields_d = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows_d.append(row)


flag = True

# for trains in stations
# for k in range(0, len(schedule)):
#     if schedule[k] == x:
#         # s = True
#         a = stations[k]
#         b = stations[k+1]
#         print("Currently Running from {} to {} ".format(a, b))
#         a_t = schedule[k]
#         b_t = schedule[k+1]
#         i_dist = 0
#         print(i_dist)
#         flag = False
#         break

# for trains not in stations
if flag:
    for k in range(0, len(schedule)):
        if schedule[k] > x:
            # s = False
            a = stations[k - 1]
            b = stations[k]
            for i in range(0, len(rows_d)):
                if a == rows_d[i][0]:
                    d_a = float(rows_d[i][1])
                if b == rows_d[i][0]:
                    d_b = float(rows_d[i][1])
            t_dist = d_b - d_a
            print("Currently Running from {} to {} ".format(a, b))
            a_t = schedule[k-1]
            b_t = schedule[k]
            # calculting total time
            time = b_t - a_t
            time = str(time)
            time = time.split(":")
            # calculating current time
            time_c = x - a_t
            time_c = str(time_c)
            time_c = time_c.split(":")
            i_dist = (t_dist / float(time[1])) * float(time_c[1])
            print(i_dist)
            flag = False
            break

loc = str(input("Enter Departing Station: "))
for i in range(0, len(rows_d)):
    if loc == rows_d[i][0]:
        d_loc = float(rows_d[i][1])
        break

c_dist = float(input("Enter Distance Covered: "))

covered_distance = c_dist + d_loc
ideal_distance = i_dist + d_a

if ideal_distance > covered_distance:
    delay = round(ideal_distance - covered_distance, 2)
    print("Train {} is {} kms behind scheduled position".format(route, delay))
    # perform mitigation
    time_r = b_t - x
    time_r = str(time_r)
    time_r = time_r.split(":")

    r_dist = d_b - covered_distance

    m_speed = (r_dist * 60) / float(time_r[1])

    str1 = "There is a major delay in the route."
    str2 = "The delay cannot be mitigated."
    str3 = "The train must maintain an average speed of"
    str4 = " kmph to minimize the delay."

    if m_speed > 90:
        m_speed = 90
        print("There is a major delay in the route.\n"
              "The delay cannot be mitigated completely.\n"
              "The train must maintain an average speed above " +str(m_speed)+ " to minimize the delay.")
        report = "There is a major delay in the route. The delay cannot be mitigated completely. The train must maintain an average speed above " +str(m_speed)+ " kmph to minimize the delay."
        with open('delay.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date.today(), x, 'Churchgate_Up', route, delay, loc, "No", report])


    else:
        print("There is a minor delay in the route.\n"
              "For the delay to be mitigated the train must maintain an average speed of {} kmph for the remaining distance.".format(round(m_speed, 2)))
        report = "There is a minor delay in the route. For the delay to be mitigated the train must maintain an average speed of" +str(round(m_speed, 2))+ "kmph"
        with open('delay.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date.today(), x, 'Churchgate_Up', route, delay, loc, "Yes", report])
else:
    print("Train {} is on time".format(route))
