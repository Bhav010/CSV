#using datetime module
#adding dates to the x axis for the month of July2018

import csv
from datetime import datetime

infile = open('sitka_weather_07-2018_simple.csv', 'r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))         #to check type for iteration

for index, column_header in enumerate(header_row):      #same as for x,y in enumerate
    print(index, column_header)

highs = []          #y-axis
dates = []          #x-axis

somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(somedate)

for row in csvfile:
    highs.append(int(row[5]))            #appending high temp
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)

print(highs)

import matplotlib.pyplot as plt
fig = plt.figure()

plt.plot(dates,highs,c="red")

plt.title("Daily temp July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()
plt.show()
