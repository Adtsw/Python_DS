name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hoursList = list()
hours = dict()

sortedHours = dict()

for line in handle:
    if 'From ' in line:
        words = line.split()
        time = words[5].split(':')
        hoursList.append(time[0])

#print(hoursList)

for hour in hoursList:
    hours[hour] = hours.get(hour,0) + 1

sortedHours = sorted([(x,y) for x,y in hours.items()])

for x,y in sortedHours:
    print(x,y)
