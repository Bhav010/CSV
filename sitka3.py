
# 1) changing the file to include all the data for the year 2018
# 2) change the title to - Daily and low high temperatures -2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between high and low

import csv
from datetime import datetime

# 1) File changed to get all 2018 data
infile = open('sitka_weather_2018_simple.csv', 'r')         

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
    highs.append(int(row[5]))            #appending high temp
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)                   
    lows.append(int(row[6]))            #appending low temp
    


print(highs)
# 3) extract low temp from file
print(lows)                            

import matplotlib.pyplot as plt
fig = plt.figure()

plt.plot(dates,highs,c="red", alpha=0.5)        # alpha is for making the color tone lighter
plt.plot(dates,lows,c="blue", alpha=0.5)        # 3)add low temp to graph/plot in blue color

# 4)color/shade the area between high and low graph
plt.fill_between(dates,highs,lows,facecolor="cyan", alpha=0.3)                

# 2) Changed the title to Daily and low high temperatures -2018
plt.title(" Daily and low high temperatures -2018", fontsize=16)            
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()
#plt.show()

#sub-plots

plt.subplot(2,1,1)    #row, col,index of subplot
plt.plot(dates,highs,c="red")
plt.title("High temp")

plt.subplot(2,1,2)    #row, col,index of subplot
plt.plot(dates,lows,c="blue")
plt.title("Low temp")

plt.suptitle("Highs and lows of Sitka")     #Title updated to show high and low temp
plt.show()