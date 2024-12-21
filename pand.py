import pandas as pd
import numpy as np

arr = np.arange(0, 20).reshape(5, 4)

# Creating dataframe
df = pd.DataFrame(data=arr, index=["R1", "R2", "R3", "R4", "R5"], columns=["C1", "C2", "C3", "C4"])
print(df)

print(df.head(2))#shows the top 5 elements in default or given in argument
print(df.tail(2))#shows the bottom 5.....

print(df.info())#shows space contains by rows and columns

print(df.describe())# show all mean , std, min , max, count , 25% , 50% , 75%  of data
#object types are not included in this function

print(df.head())

#indexing :- accessing the elements using diff methods 
#types of indexing:- columnname , rowindex[loc] , iloc[];

print(df[["C2","C3","C4"]]) #columnname :- access columns of data and multiple columns always in nested list.

print(df.loc[["R1" , "R3" , "R4"]])#row indexing 

print(df.iloc[2:4,0:2])#element indexing to access elements of data

#conveting dataframe into arrays
#print(df.iloc[0:,1:].values)

#basic operations

df.drop_duplicates(subset=['email']) #deleted duplicate elements of selected feild

 
rem = pd.DataFrame(data=[[1,np.nan,3],[4,5,6]], index=["R1", "R2"], columns=["C1", "C2", "C3"])
print(rem.isnull()) #show if a null value exist in data

print(rem.isnull().sum())#shows 1 where the null exist row or column.

print(df[["C2","C3","C4"]].value_counts())#shows how many  times a unique  element is present.

print(df[["C2","C3","C4"]].nunique())#show no. of unique elemets present in rows and columns

print(df["C2"].unique())#shows unique elemets in an row or column

print(df[df["C2"]>2]) #showing rows having elements larger then 2
