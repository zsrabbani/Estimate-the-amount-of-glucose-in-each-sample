# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 14:50:59 2018

@author: MHA
"""

import matplotlib.pyplot as plt
import numpy as np
import math

my_file=open('PlotFile.txt','r')
data=my_file.readlines()
counter=0
glucose=[]
averages=[]
standard_deviation=[]
avg=0  #  Average Temp
cnt=0

#  Calculating Averages
for i in data:
    if counter%2==0:
        if len(glucose)>0:
            if float(data[counter])==glucose[-1]:
                avg+=float(data[counter+1])
                cnt+=1
            else:
                averages.append(avg/cnt)
                print('average for glucose '+str(glucose[-1])+'is :'+str(averages[-1]))
                avg=0
                print('avg: glucose='+str(data[counter]))
                #print('avg: glucose='+str(data[counter]))
                cnt=1
                glucose.append(float(data[counter]))
                avg+=float(data[counter+1])    
        else:
            cnt=1
            glucose.append(float(data[counter]))
            avg+=float(data[counter+1])    
    counter+=1

averages.append(avg/cnt)  #  for the last one it comes out of for without appending averages
    
fig=plt.figure(1)
fig.patch.set_facecolor('white')
ax1=fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.patch.set_facecolor('c')
ax1.plot(glucose,averages,'ro')
for label in ax1.get_xticklabels():
    label.set_color('green')
for label in ax1.get_yticklabels():
    label.set_color('green')
ax1.set_xlabel('Glucose Density (mMole)')
ax1.set_ylabel('Average of Channel Pixels')
fig.savefig('Average.pdf')
fig.savefig('Average.png')
plt.show()


s=0  #  Standard Deviation Temp
cnt=0
counter=0
index=0
#  Calculating Standard Deviation
for i in data:
    if counter%2==0:
        if float(data[counter])==glucose[index]:
            s+=((float(data[counter+1])-float(averages[index]))**2)
            cnt+=1
        else:
            standard_deviation.append(math.sqrt(s/cnt))
            s=0
            cnt=1
            index+=1
            s+=((float(data[counter+1])-float(averages[index]))**2)
    counter+=1

standard_deviation.append(math.sqrt(s/cnt))




fig=plt.figure(2)
fig.patch.set_facecolor('white')
ax1=fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.patch.set_facecolor('c')
ax1.plot(glucose,standard_deviation,'bo')
for label in ax1.get_xticklabels():
    label.set_color('green')
for label in ax1.get_yticklabels():
    label.set_color('green')
ax1.set_xlabel('Glucose Density (mMole)')
ax1.set_ylabel('Standard Deviation of Instances of Same Density')
fig.savefig('StandardDeviation.pdf')
fig.savefig('StandardDeviation.png')
plt.show()
