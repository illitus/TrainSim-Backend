def dashboard_vircg(request):
    cg_up = "statics/csv/churchgate_up.csv"
    stat = "statics/csv/distance_up.csv"
    # initializing the titles and rows list
    transit = []
    new_schedule = []
    fields = []
    rows = []
    # print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        # print("Total no. of rows: %d" % csvreader.line_num)
    statfields = []
    statlist = []
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    # fetching current time
    x = datetime.now()
    # x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule = []
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
            # print("running: ", rows[i][0])
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_up(schedule, stations, x)

                    details.append(stations[k].upper())
                    details.append(10 + statlist.index(stations[k]) * 37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_up(schedule, stations, x)
                        details.append(stations[k - 1].upper())
                        details.append(10 + statlist.index(stations[k - 1]) * 37.5)
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                else:
                    details.append('----:----')

            new_schedule.append(details)
    ziplist = zip(transit, new_schedule)
    return render(request, "dashboard/vircg.html", {'timenow': x, 'ziplist': ziplist})