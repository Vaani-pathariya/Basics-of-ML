#all things data visualisation
from tkinter.tix import ListNoteBook
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[0,1,2,3,4,5]
y=[0,2,4,6,8,10]
plt.figure(figsize=(5,3),dpi=100)# this resizes the given graph , 
#shorthand notation: fmt='[color][marker][line]
plt.plot(x,y,label='2x',linestyle='--',color='red',linewidth=1,marker='.',markersize=10,markeredgecolor="blue")
plt.title("MY FIRST GRAPH!",fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])#this changes the scale of the given axis depending upon the values provided 
plt.legend()#the label becomes shown after adding this function
x2=np.arange(0,4,0.5)
plt.plot(x2[:6],x2[:6]**2)
#overlapping is also allowed
plt.plot(x2[5:],x2[5:]**2,'r--')
print(x2)
plt.savefig('mygraph.png',dpi=100)
#Barcharts
labels=['A','B','C']
values=[1,4,2]
bars=plt.bar(labels,values)
bars[0].set_hatch('/')

#histogram
bins=[40,50,60,70,80,90,100]
fifa=pd.read_csv('fifa_data.csv')
plt.hist(fifa.Overall,bins=bins,color='red')
left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
labels=['Left','Right']
explode=(.1,.1)
#plt.pie([left,right],labels=labels,autopct='%.2f%%',pctdistance=0.8,explode=explode)
bar=fifa.loc[fifa.Club=='FC Barcelona']['Overall']
mad=fifa.loc[fifa.Club=='Real Madrid']['Overall']
plt.boxplot([bar,mad])
plt.show()

