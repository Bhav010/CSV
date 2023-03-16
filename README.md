# matplotlib_csv
Advanced Python - Matplotlib - using CSV files

(this project is to teach students how to use CSV files in python, 
this project also teaches students how to visualize the data using matplotlib)


In the 5th file:  

We have used the concept of automatic indexes. Earlier we had hard coded the indexes corresponding to the TMIN and TMAX columns. In the 5th file, we have used the header row to determine the indexes for these values, so the program can work
for Sitka or Death Valley. We have used the station name to automatically generate an appropriate title for the graphs.

2 subplot graphs are created in one visualization, we can see both graphs to compare side by side.

function called subplots() has been used from Matplotlib's pyplot API. It has a convenience which acts as a
utility wrapper and helps in creating common layouts of subplots, including the enclosing figure object, in a single call.

