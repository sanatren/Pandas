# we will learn about reading different files in panda 
#reading csv_files from pandas
#also using stingIO

from io import StringIO
import pandas as pd

df = pd.read_csv('student.csv')

#print(df.head())

data = ('col1,col2,col3\n'
        'x,y,1\n'
        'a,b,2\n') #creating data


print(StringIO(data)) #converted in memory file format object from string.

td = pd.read_csv(StringIO(data)) #coverted to data format from string.

print(pd.read_csv(StringIO(data),usecols={'col1','col2'}))#creating data for the selected columns.

td.to_csv('test1',index = False) #saving the files to scv format without index (csv files contains index of themseleves)

print(type(td))

data1 = ('col1,col2,col3,col4\n'
        'x,y,1,2\n'
        'a,b,2\n') #last value was not provided so null will be assigned there.
td1 = pd.read_csv(StringIO(data1))
print(td1)

print(td1['col1'][0])
print(td1.iloc[0:,3])
print(td1.loc[1:])

print(td1.isnull())
print(td1.isnull().sum())


#print(pd.read_csv(StringIO(data1),index_col=0)) # making columns as index 

print(pd.read_csv(StringIO(data1),usecols={'col1','col2'},index_col=0))

#print(pd.read_csv('bls.csv',sep = '\t'))

bf = pd.read_csv(StringIO(data1),dtype ={'x':int , 'y':float , '1':str })#assignong data types to elements.
print(bf.info())

td2 = pd.read_csv('bls.csv',sep = '\t')
td2.to_csv('savebls',index=False)