#Daily high temperature graph for July 2018

import csv

infile = open('sitka_weather_07-2018_simple.csv', 'r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))         #to check the type for iteration

for index, column_header in enumerate(header_row):      #same as for x,y in enumerate
    print(index, column_header)

highs = []

for row in csvfile:
    highs.append(int(row[5]))            #appending high temp

print(highs)

import matplotlib.pyplot as plt
plt.plot(highs,c="red")                             #high temp, color=red
plt.title("Daily temp July 2018", fontsize=16)      #Graph/plot title
plt.xlabel("", fontsize=16)                         #label x-axis
plt.ylabel("Temperature(F)", fontsize=16)           ##label y-axis
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()      #generates the graph/plot
