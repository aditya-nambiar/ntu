import matplotlib.pyplot as plt
import matplotlib
import datetime
import random
import time
import numpy

import sys
arg = sys.argv[1]
f = open('../data/April Data.csv', 'r')
line = f.readline()
line = f.readline()
vals = []
xdates = []

flag = 0
plt.xlabel('Time')
plt.ylabel('Power Consumed')
plt.title('Graph')
plt.legend()
st_dt = ""
arg1 =1
if arg == "mon":
    arg1 = 0
elif arg == "tue":
    arg1 = 1
elif arg == "wed":
    arg1 = 2
elif arg == "thur":
    arg1 = 3
elif arg == "fri":
    arg1 = 4
elif arg == "sat":
    arg1 = 5
elif arg == "sun":
    arg1 = 6

xdates = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
while line:
    arr = line.split(',');
    dt =datetime.datetime.strptime(arr[2],"%d-%b-%y %H:%M:%S")
   
    if dt.weekday() == arg1 and flag == 0:
        vals = vals + [arr[8]]
        flag = 1
        st_dt = dt.date()
      
    elif dt.weekday() == arg1 and flag == 1:        
        vals = vals + [arr[8]]
    elif dt.weekday() != arg1 and flag == 1: #day stopped        
        flag =0    
        if len(vals) == 24:
            plt.plot(xdates,vals,linestyle='-', color=numpy.random.rand(3,1),label=st_dt)
            max1 =0.0
            pt1 =0
            print(vals)
            for x in range(0,24):
               prev = max1    
               max1 = max(max1,float(vals[x]))
               if prev != max1:
                   pt1 =  x
              
            plt.plot([pt1],[max1],'ro') 
            
        vals =[]
        
        
    line = f.readline()
    
f.close()

#xdates = [datetime.datetime.strptime(date,"%d-%b-%y %H:%M:%S") for date in dates]
#plt.plot_date(xdates,vals,linestyle='-', color='r',)
plt.legend()

plt.show()
