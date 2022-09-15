import numpy as np
import pandas as pd

dic1={
    "name":['Vaani','Bebo','Mumma','Daddy'],
    "marks":[92,43,89,89],
    "city":['chandigarh','ghaziabad','kanpur','kanpur']
}
df=pd.DataFrame(dic1)#converts the data given into a table of values
df.to_csv('friends.csv')#this converts the formed table to a csv file that is viewed in excel
print(df)
df.to_csv('changed.csv',index=False)#this makes a csv without the indexing
print(df.head(2))#prints the top 2 lines of data
print(df.tail(3))#prints the bottom 3 lines of data
print(df.describe())#prints the max,mean ,standard deviation,and many other kinds of data from the given numerical data columns
table=pd.read_csv('vaani.csv')
table['Speed'][0]=50
table.index=['first','second','third','fourth']
print(table)
#fun fact,numpy is written in c language providing the speed for execution
#in a dataframe , a single column has the same data type
ser=pd.Series(np.random.rand(34))
ser=pd.DataFrame(np.random.rand(334,5))
ans=ser.to_numpy()
print (ser)
ser.T#this statement does a transpose of the given datafield
#axis=0 means rows and axis =1 means colums
ser.sort_index(axis=0,ascending=False)
ser[0]#this prints the first column of the data frame
print(ans)
ser.loc[0,0]=342
ser.drop(0,axis=1)#this command drops the column(since it is axis=1) with the given index value
ser.loc[[1,2],['C','D']]#loc function just returns a copy
ser.iloc[0,.4]#whenever you want to denote exclusively the index and not 'A',etc
ser.drop(['A','C'],axis=1,inplace =True)#this changes the original data frame
ser.reset_index(drop=True,inplace=True)#this resets the indexing of the dataframe given since the indexing may change because of several things performed on the data frame
ser['B'].isnull()#outputs true if the value is null at particular position in the array(intdividual)
#whenever you are changing any data set gaanth baandth lo use loc
ser.info()#this is A method to tell us about the dataframe
ser['name'].value_counts(dropna=False)#show the count of the different values in a give column
ser.isnull() 

tb=pd.read_csv('test.csv')
tb.describe()
tb.mean()
tb.corr()
tb.count()
tb.max()
tb.min()
tb.median()
tb.std()
data=pd.read_excel('data.xlsx',sheet_name='Sheet2')
#this reaquires to pip install xlrd then no error is flashed
data.to_excel('data.xlsx',sheet_name='Sheet2')
#this saves the data into an excel sheet and this may require the installation of a package 