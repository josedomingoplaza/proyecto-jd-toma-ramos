import csv
import datetime

def GetCourseRows(NRC):
    i = 0
    for a in data:
        if a[2] == NRC:
            i += 1
    return i

def CheckCompatibility(course1, course2):
    schedule1 = []
    for a in data:
        if a[2] == str(course1):
            schedule1.append(a[10:16])

    times1 = []

    for a in schedule1:
        row = []
        for b in a:
            if len(b) > 0:
                row.append([datetime.time(int(b[0:2]), int(b[3:5])), datetime.time(int(b[7:9]), int(b[10:12]))])
            else:
                row.append("")

        times1.append(row)

    schedule2 = []
    for a in data:
        if a[2] == str(course2):
            schedule2.append(a[10:16])
    
    times2 = []

    for a in schedule2:
        row = []
        for b in a:
            if len(b) > 0:
                row.append([datetime.time(int(b[0:2]), int(b[3:5])), datetime.time(int(b[7:9]), int(b[10:12]))])
            else:
                row.append("")

        times2.append(row)

    days1 = {"monday":[], "tuesday":[], "wednesday":[], "thursday":[], "friday":[], "saturday":[]}

    for a in range(len(times1)):
        for b in range(len(times1)):
            if b == 0 and (times1[a][b] not in days1["monday"]): 
                days1["monday"].append(times1[a][b])
            if b == 1 and (times1[a][b] not in days1["tuesday"]):
                days1["tuesday"].append(times1[a][b])
            if b == 2 and (times1[a][b] not in days1["wednesday"]):
                days1["wednesday"].append(times1[a][b])
            if b == 3 and (times1[a][b] not in days1["thursday"]):
                days1["thursday"].append(times1[a][b])
            if b == 4 and (times1[a][b] not in days1["friday"]):
                days1["friday"].append(times1[a][b])
            if b == 5 and (times1[a][b] not in days1["saturday"]):
                days1["saturday"].append(times1[a][b])

    keys = days1.keys()
    for a in keys:
        if "" in days1[a]:
            days1[a].remove('')


    days2 = {"monday":[], "tuesday":[], "wednesday":[], "thursday":[], "friday":[], "saturday":[]}

    for a in range(len(times2)):
        for b in range(len(times2)):
            if b == 0 and (times2[a][b] not in days2["monday"]): 
                days2["monday"].append(times2[a][b])
            if b == 1 and (times2[a][b] not in days2["tuesday"]):
                days2["tuesday"].append(times2[a][b])
            if b == 2 and (times2[a][b] not in days2["wednesday"]):
                days2["wednesday"].append(times2[a][b])
            if b == 3 and (times2[a][b] not in days2["thursday"]):
                days2["thursday"].append(times2[a][b])
            if b == 4 and (times2[a][b] not in days2["friday"]):
                days2["friday"].append(times2[a][b])
            if b == 5 and (times2[a][b] not in days2["saturday"]):
                days2["saturday"].append(times2[a][b])

    for a in keys:
        if "" in days2[a]:
            days2[a].remove('')

    for key in keys:
        if len(days1[key]) != 0 or len(days2[key]) != 0:
            for a in days1[key]:
                for b in days2[key]:
                    if (a[1] <= b[0]) or (b[1] <= a[0]):
                        pass
                    else:
                        return False

    return True

data = []

with open("Horarios.csv", "r", encoding="utf-8") as csvfile:
    rows = csv.reader(csvfile, delimiter=",")

    for a in rows: data.append(a)

print(CheckCompatibility(3899, 6945))