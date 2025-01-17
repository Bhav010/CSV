
# 2 subplot graphs in one visualization 
# to see both graphs to compare side by side

import csv
from datetime import datetime

#Open both sitka and deathvalley files
infile1 = open('sitka_weather_2018_simple.csv', 'r')
infile2 = open('death_valley_2018_simple.csv', 'r')         

csvfile1 = csv.reader(infile1)
csvfile2 = csv.reader(infile2)

header_row1 = next(csvfile1)
header_row2 = next(csvfile2)

#print(type(header_row1))         #to check type of Sitka-2018 for iteration
#print(type(header_row2))         #to check type of Death-Valley for iteration

#iterate through Sitka-2018 file

#for index, column_header in enumerate(header_row1):      #same as for x,y in enumerate
#    print(index, column_header)

highs1 = []          #y-axis
dates1 = []          #x-axis
lows1 = []

#somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(somedate)

for row1 in csvfile1:
    #while True:
    try:
        highs1.append(int(row1[5]))            #appending high temp from sitka weather file
        thedate = datetime.strptime(row1[2],'%Y-%m-%d')
        dates1.append(thedate)                   
        lows1.append(int(row1[6]))            #appending low temp
    except:
        print()
        # print(f"There was an error on record: {row1}")
    else:
        continue


#iterate through Death-Valley file

#for index, column_header in enumerate(header_row2):      #same as for x,y in enumerate
#    print(index, column_header)

highs = []          #y-axis
dates = []          #x-axis
lows = []

#somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(somedate)

for row2 in csvfile2:
    try:
        highs.append(int(row2[4]))            #appending high temp from sitka weather file
        thedate = datetime.strptime(row2[2],'%Y-%m-%d')
        dates.append(thedate)                   
        lows.append(int(row2[5]))            #appending low temp
    except:
        print()
        # print(f"There was an error on record: {row2}")
    else:
        continue


import matplotlib.pyplot as plt
fig = plt.figure()

fig.autofmt_xdate()

#sub-plots

plt.suptitle(f"Temperature comparison between {row1[1]} and {row2[1]}")     #Main title

#sub-plot-1 for Sitka

plt.subplot(2,1,1)    #row, col,index of subplot
plt.plot(dates,highs1,c="red")
plt.plot(dates,lows1,c="blue")
plt.fill_between(dates1,highs1,lows1,facecolor="blue", alpha=0.2)  
plt.title(row1[1])          #sub-plot1 title
   
#sub-plot-2 for Death Valley

plt.subplot(2,1,2)    #row, col,index of subplot
plt.plot(dates,highs,c="red")
plt.fill_between(dates,highs,lows,facecolor="blue", alpha=0.2)  
plt.plot(dates,lows,c="blue")
plt.title(row2[1])      ##sub-plot2 title

plt.show()