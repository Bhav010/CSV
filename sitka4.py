
# 1) handle error checking using try and except
# 2) change file to use death valley data


import csv
from datetime import datetime

infile = open('death_valley_2018_simple.csv', 'r')         # 2) file changed to death valley

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))         #to check type for iteration

for index, column_header in enumerate(header_row):      #same as for x,y in enumerate
    print(index, column_header)

highs = []          #y-axis
dates = []          #x-axis
lows = []

somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(somedate)

for row in csvfile:
    #while True:
    try:                                    # 1) handle error checking using try and except
        highs.append(int(row[4]))            #appending high temp
        thedate = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(thedate)                   
        lows.append(int(row[5]))            #appending low temp
    except:
            #pass
        print(f"There was an error on record: {row}")
    else:
        continue


print(highs)
print(lows)

import matplotlib.pyplot as plt
fig = plt.figure()

plt.plot(dates,highs,c="red", alpha=0.5)        # alpha is for making the color tone lighter
plt.plot(dates,lows,c="blue", alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor="blue", alpha=0.2)                

plt.title(" Daily and low high temperatures -2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()
plt.show()

